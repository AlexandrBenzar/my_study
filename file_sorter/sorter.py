# -*- coding: utf-8 -*-

import os, time, shutil
import zipfile
from abc import ABC, abstractmethod


class Sorter(ABC):
    def __init__(self, file_name):
        self.file_name = file_name

    def execute(self):
        for dir_path in self.get_files_path():
            final_path = self.destination_path(dir_path)
            self.make_dir(final_path)
            self.copy(dir_path, final_path)

    @abstractmethod
    def get_files_path(self):
        pass

    @abstractmethod
    def destination_path(self, full_file_path):
        pass

    def make_dir(self, path):
        os.makedirs(path, exist_ok=True)

    @abstractmethod
    def copy(self, src, dst):
        pass


class SortingFromFile(Sorter):

    def get_files_path(self):
        norm_path = os.path.normpath(self.file_name)
        files_paths_list = []

        for dirpath, _, filenames in os.walk(norm_path):
            for file in filenames:
                files_paths_list.append(os.path.join(dirpath, file))
        return files_paths_list

    def destination_path(self, full_file_path):
        file_time = time.gmtime(os.path.getmtime(full_file_path))
        return os.path.join('icons_by_year', str(file_time[0]), str(file_time[1]), str(file_time[2]))

    def copy(self, src, dst):
        shutil.copy(src, dst)


class SortingFromZip(Sorter):
    def __init__(self, file_name):
        super().__init__(file_name=file_name)
        self.zip_file = zipfile.ZipFile(self.file_name, 'r')

    def get_files_path(self):
        files_paths_list = []
        for file in self.zip_file.namelist():
            filename = os.path.basename(file)
            if filename:
                files_paths_list.append(file)

        return files_paths_list

    def destination_path(self, full_file_path):
        date = self.zip_file.getinfo(full_file_path).date_time
        return os.path.join('icons_by_ear_from_zip', str(date[0]), str(date[1]), str(date[2]))

    def copy(self, src, dst):
        member = self.zip_file.open(src)
        filename = os.path.basename(src)
        final_path_with_file = os.path.join(dst, filename)
        with open(final_path_with_file, 'wb') as ff:
            shutil.copyfileobj(member, ff)


z_file = 'icons.zip'
file = 'icons'
sort_from_zip = SortingFromZip(file_name=z_file)
sort_from_file = SortingFromFile(file_name=file)

sort_from_zip.execute()
sort_from_file.execute()
