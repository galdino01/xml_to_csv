from cxml import xml_to_csv
            
if __name__ == '__main__':
    import sys
    import os
    
    try:
        file_path = sys.argv[1]
        csv_name = sys.argv[2]
        show_process = sys.argv[3]
    except IndexError:
        sys.exit("Argumentos obrigatórios estão em falta.")
        

    if os.path.isfile(file_path):
        field_names = ['title', 'author', 'img', 'slug', 'content', 'excerpt', 'categories']

        xml_to_csv(file_path, csv_name, field_names, show_process)
    else:
        sys.exit(f"Caminho não encontrado: {file_path}")