def main():

    from path import Path

    dir_path = Path("test_dir")
    dir_path.mkdir_p()

    file_path = dir_path / "hello.txt"
    file_path.write_text("Bonjour depuis path.py !")

    content = file_path.read_text()
    print("Contenu du fichier :", content)

if __name__ == '__main__':
    main()