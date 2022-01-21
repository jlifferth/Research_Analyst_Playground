from subprocess import STDOUT, check_call, check_output


def install_java_scala():
        try:
          java_ver = check_output(['java', '-version'], stderr=STDOUT)
          print(java_ver)
        except:
          java_ver = b''
        try:
          scala_ver = check_output(['scala', '-version'], stderr=STDOUT)
        except:
          scala_ver = b''
        if b'1.8.0_232' not in java_ver:
          java_8_install = ['apt-get', '--quiet', 'install',
                            '-y', 'openjdk-8-jdk-headless']
          java_set_alt = ['update-alternatives', '--set', 'java', 
                          '/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java' ] 
          check_call(java_8_install, stdout=open(os.devnull, 'wb'), 
                     stderr=STDOUT)
          os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64" 
          check_call(java_set_alt)  
        if b'2.11.12' not in scala_ver:
          scala_install = ['apt-get', '--quiet', 'install', 'scala']
          check_call(scala_install)


import os


# download SRA tool kit
def setup_sra_tool(url):
    !wget $url
    !gunzip
    sratoolkit
    .2
    .9
    .6 - 1 - ubuntu64.tar.gz
    !tar - xf
    sratoolkit
    .2
    .9
    .6 - 1 - ubuntu64.tar


# download SRA file and extract fastq
def get_sra(url, sra_path):
    os.chdir('/content')
    !wget $url
    sra_name = url[-11:]
    os.chdir(sra_path)
    !./ fastq - dump / content /$sra_name - O / content /
    os.chdir('/content')


# url of SRA tool kit
url_tk = 'https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.6-1/sratoolkit.2.9.6-1-ubuntu64.tar.gz'
setup_sra_tool(url_tk)

# example SRA file
sra_url = 'https://sra-download.ncbi.nlm.nih.gov/traces/era6/ERR/ERR3014/ERR3014700'
tool_path = '/content/sratoolkit.2.9.6-1-ubuntu64/bin'
get_sra(sra_url, tool_path)