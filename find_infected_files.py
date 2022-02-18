from installed_softwares import RegistryConnection
from installed_softwares import InstalledSoftware


class FindFiles:
    def __init__(self):
        self.reg_conn = RegistryConnection()
        self.inst_sftw = InstalledSoftware()

    def dir_file_list(self):
        return self.inst_sftw.dump_software_lst_to_json(
            ['DisplayName', 'InstallLocation', 'InstallSource', 'UninstallString'],
            'name_dir.json', False)

    def sftw_name_to_dir(self, sftw_name):  # Enter DisplayName as in the registry
        lst = self.dir_file_list()
        for i in range(len(lst[0])):
            index = lst[0].index(sftw_name)
            for j in range(1, 4):
                if lst[j][index]:
                    if j != 3:
                        return lst[j][index]
                    else:  # Removing the last '\\' in the string
                        splitted = lst[j][index].split('\\')
                        splitted = splitted[:-1]
                        return '\\'.join(splitted).replace('"','')
        return 'NO PATH'

    



