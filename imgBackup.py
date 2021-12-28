import os
import shutil
from pathlib import Path


class BackupDir:
    """BackupDir
    PATHに指定したバックアップ用ディレクトリを作成する
    """
    PATH = "/tmp/sd"

    @classmethod
    def make(cls):
        os.makedirs(cls.PATH, exist_ok=True)


class Logger:
    """Logger
    PATH/copy.logに、バックアップ作業ログを記録する
    """
    # Logger.log("hoge") >> backupdir/copy.log
    FILE = Path(BackupDir.PATH).joinpath("copy.log")

    @classmethod
    def log(cls, message):
        print(message)
        with open(cls.FILE, mode='a+') as f:
            f.write(message + os.linesep)


class ImgBackup:
    """ImgBackup
    ~/tmp/*.[画像用拡張子]のファイルをバックアップする
    .で始まる隠しファイルはバックアップの対象外
    """
    backup_target_list = []

    def backup(self):

        BackupDir.make()
        self.__make_backup_list()
        self.__copy()

    def __copy(self):
        for target in self.backup_target_list:
            try:
                shutil.copy2(target, BackupDir.PATH)
                Logger.log("Copy " + str(target))
            except PermissionError:
                Logger.log(
                    "no permission to copy the file: " + str(target))

    def __make_backup_list(self):
        all_file_list = []
        # backup img file in ~/tmp/*
        for dir, _, files in os.walk(Path.home().joinpath("tmp")):
            for file in files:
                all_file_list.append(Path(dir).joinpath(file))

        for path in all_file_list:
            if self.__is_include_hidden(path):
                continue
            if self.__is_img(path):
                self.backup_target_list.append(path)
                # print(path)

    def __is_include_hidden(self, path):
        """ __is_include_hidden
      　　隠しファイル/隠しフォルダかどうか判定
        """

        # 絶対パス中の各名前が、.で始まっていたら無視したい
        path_parts = Path(path).parts
        for part in path_parts:
            if part.startswith("."):
                return True
            else:
                return False

    def __is_img(self, path):
        """ __is_img
        指定した画像拡張子を持つかどうか判定
        """
        img_ext_list = [".jpg", "png", "gif"]
        return Path(path).suffix in img_ext_list


class Main:
    def run(self):
        img_backup = ImgBackup()
        img_backup.backup()


if __name__ == "__main__":

    BackupDir.make()
    Logger.log("test")
    main = Main()

    main.run()
