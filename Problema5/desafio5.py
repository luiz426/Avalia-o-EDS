import mysql.connector
import csv
import os
from typing import List, Dict, Any


def parse_layout(layout_path):
    columns = []
    with open(layout_path, encoding="latin1") as f:
        reader = csv.DictReader(f)
        for row in reader:
            col_name = row["Coluna"].strip()
            start = int(row["Inicio"])
            end = int(row["Fim"])
            tipo = row["Tipo"].strip().upper()
            # Map types
            if "CHAR" in tipo or "VARCHAR" in tipo:
                mysql_type = "VARCHAR(255)"
            elif "NUMBER" in tipo:
                mysql_type = "DOUBLE"
            else:
                mysql_type = "VARCHAR(255)"
            columns.append({
                "name": col_name,
                "start": start,
                "end": end,
                "mysql_type": mysql_type,
            })
    return columns


def create_table(conn, cursor, table_name, columns):
    col_defs = [f"`{col['name']}` {col['mysql_type']}" for col in columns]
    sql = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({', '.join(col_defs)});"
    cursor.execute(sql)
    conn.commit()


def convert_value(val):
    text = val.strip()
    return text if text != "" else None


def load_data(conn, cursor, table_name, columns, data_path):
    col_names = [col["name"] for col in columns]
    placeholders = ", ".join(["%s"] * len(col_names))
    insert_sql = f"INSERT INTO `{table_name}` ({', '.join(col_names)}) VALUES ({placeholders});"

    with open(data_path, encoding="latin1") as f:
        lines = f.readlines()

    for line in lines:
        values = []
        row_data = {}
        for col in columns:
            raw = line[col["start"] - 1: col["end"]]
            val = convert_value(raw)
            values.append(val)
            row_data[col["name"]] = val

        # Validar dependências de foreign key
        try:
            if table_name.lower() == "rl_procedimento_cid":
                cursor.execute("""
                    SELECT 1 FROM staging.tb_procedimento
                    WHERE CO_PROCEDIMENTO = %s AND DT_COMPETENCIA = %s
                """, (row_data["CO_PROCEDIMENTO"], row_data["DT_COMPETENCIA"]))
                if cursor.fetchone() is None:
                    continue

                cursor.execute("""
                    SELECT 1 FROM staging.tb_cid
                    WHERE CO_CID = %s
                """, (row_data["CO_CID"],))
                if cursor.fetchone() is None:
                    continue

            if table_name.lower() == "tb_forma_organizacao":
                cursor.execute("""
                    SELECT 1 FROM staging.tb_sub_grupo
                    WHERE CO_GRUPO = %s AND CO_SUB_GRUPO = %s AND DT_COMPETENCIA = %s
                """, (
                    row_data["CO_GRUPO"], row_data["CO_SUB_GRUPO"], row_data["DT_COMPETENCIA"]
                ))
                if cursor.fetchone() is None:
                    continue

            cursor.execute(insert_sql, values)
        except Exception as e:
            print(f"[ERRO] Linha ignorada em {table_name}: {e}")
    conn.commit()


def main():
    # CONFIGURAÇÃO DO BANCO
    db_config = {
        "host": "localhost",
        "user": "user",
        "password": "password",
        "database": "name"
    }

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
    except mysql.connector.Error as err:
        print(f"[ERRO] Falha na conexão com o banco de dados MySQL: {err}")
        return

    base_dir = os.path.dirname(os.path.abspath(__file__))
    layout_files = [f for f in os.listdir(base_dir) if f.endswith("_layout.txt")]

    # Ordem de prioridade para respeitar as foreign keys
    ordem_prioridade = [
        "tb_grupo",
        "tb_sub_grupo",
        "tb_forma_organizacao",
        "tb_procedimento",
        "tb_cid",
        "rl_procedimento_cid"
    ]

    for base in ordem_prioridade:
        layout_filename = base + "_layout.txt"
        data_filename = base + ".txt"

        layout_path = os.path.join(base_dir, layout_filename)
        data_path = os.path.join(base_dir, data_filename)

        if not os.path.isfile(layout_path) or not os.path.isfile(data_path):
            print(f"[AVISO] Layout ou dados não encontrados para: {base}")
            continue

        try:
            print(f"[INFO] Processando: {layout_filename} + {data_filename} -> Tabela: {base}")
            columns = parse_layout(layout_path)
            create_table(conn, cursor, base, columns)
            load_data(conn, cursor, base, columns, data_path)
        except Exception as e:
            print(f"[ERRO] Falha ao processar {layout_filename}: {e}")

    # Mostrar tabelas
    print("\nTabelas carregadas no banco de dados MySQL:")
    cursor.execute("SHOW TABLES;")
    for (table_name,) in cursor.fetchall():
        print(f"- {table_name}")

    cursor.close()
    conn.close()
    print(f"\n[OK] Dados inseridos no banco MySQL com sucesso.")


if __name__ == "__main__":
    main()
