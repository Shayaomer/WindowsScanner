from installed_softwares import InstalledSoftware
from xmlParser import CpeXmlParser
from matching_cve_cpe import MatcherCveCpe
from download_db import DownloadDb
import download_db
import socket


def execute():
    print('Initializing the scan & matching process...')
    print("Downloading CVE data...")
    a = DownloadDb()
    print("Downloading CPE data...")
    download_db.download_file()
    download_db.unzip_file('official-cpe-dictionary_v2.3.xml.zip', directory_to_extract=None)

    print('Getting installed softwares...')
    i_s = InstalledSoftware()
    i_s.dump_software_lst_to_json(["Publisher", 'DisplayVersion', 'DisplayName'])

    print('Parsing the CPE data...')
    b = CpeXmlParser('official-cpe-dictionary_v2.3.xml')
    b.csv_creator('official-cpe-dictionary_v2.3.xml')

    c = MatcherCveCpe()
    res_json = c.match_cve_cpe()
    return {'_id': socket.gethostname(),
            '_data': res_json}
