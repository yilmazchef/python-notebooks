from subprocess import check_output, CalledProcessError, call

# create functions for mostly common commands

def get_comp_name():
    return check_output(['hostname']).decode('utf-8').strip('\n')

def get_ip():
    return check_output(['ipconfig']).decode('utf-8').split('\n')[1].split(':')[1].strip(' ')

def get_mac():
    return check_output(['getmac']).decode('utf-8').split('\n')[1].split(' ')[-1]

def get_os():
    return check_output(['ver']).decode('utf-8').split('\n')[1].strip('\r')

def get_user():
    return check_output(['whoami']).decode('utf-8').strip('\n')

def get_wifi():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[4].split(':')[1].strip(' ')

def get_wifi_ip():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[5].split(':')[1].strip(' ')

def get_wifi_mac():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[6].split(':')[1].strip(' ')

def get_wifi_name():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[7].split(':')[1].strip(' ')

def get_wifi_status():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[8].split(':')[1].strip(' ')

def get_wifi_type():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[9].split(':')[1].strip(' ')

def get_wifi_channel():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[10].split(':')[1].strip(' ')

def get_wifi_signal():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[11].split(':')[1].strip(' ')

def get_wifi_noise():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[12].split(':')[1].strip(' ')

def get_wifi_rate():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[13].split(':')[1].strip(' ')

def get_wifi_bss():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[14].split(':')[1].strip(' ')

def get_wifi_phy():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[15].split(':')[1].strip(' ')

def get_wifi_security():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[16].split(':')[1].strip(' ')

def get_wifi_auth():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[17].split(':')[1].strip(' ')

def get_wifi_cipher():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[18].split(':')[1].strip(' ')

def get_wifi_beacon():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[19].split(':')[1].strip(' ')

def get_wifi_rssi():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[20].split(':')[1].strip(' ')

def get_wifi_link_quality():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[21].split(':')[1].strip(' ')

def get_wifi_tx_rate():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[22].split(':')[1].strip(' ')

def get_wifi_rx_rate():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[23].split(':')[1].strip(' ')

def get_wifi_network_type():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[24].split(':')[1].strip(' ')

def get_wifi_channel_utilization():
    return check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[25].split(':')[1].strip(' ')

def get_wifi_passwords():
    
    profiles = []
    try: 
        data = check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    except CalledProcessError as e:
       pass
    
    for i in profiles:
        results = check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError as e:
            pass
            
def get_disk_info():
    return check_output(['wmic', 'diskdrive', 'get', 'model,interfaceType,size']).decode('utf-8').split('\n')

def get_disk_model():
    return check_output(['wmic', 'diskdrive', 'get', 'model']).decode('utf-8').split('\n')

def get_disk_interface():
    return check_output(['wmic', 'diskdrive', 'get', 'interfaceType']).decode('utf-8').split('\n')

def get_disk_size():
    return check_output(['wmic', 'diskdrive', 'get', 'size']).decode('utf-8').split('\n')

def get_disk_serial():
    return check_output(['wmic', 'diskdrive', 'get', 'serialnumber']).decode('utf-8').split('\n')

def get_disk_firmware():
    return check_output(['wmic', 'diskdrive', 'get', 'firmwarerevision']).decode('utf-8').split('\n')

def get_disk_manufacturer():
    return check_output(['wmic', 'diskdrive', 'get', 'manufacturer']).decode('utf-8').split('\n')

def get_disk_status():
    return check_output(['wmic', 'diskdrive', 'get', 'status']).decode('utf-8').split('\n')

def get_disk_index():
    return check_output(['wmic', 'diskdrive', 'get', 'index']).decode('utf-8').split('\n')

def get_disk_partitions():
    return check_output(['wmic', 'partition', 'get', 'name,size,description,deviceid']).decode('utf-8').split('\n')

def get_disk_partition_name():
    return check_output(['wmic', 'partition', 'get', 'name']).decode('utf-8').split('\n')

def get_disk_partition_size():
    return check_output(['wmic', 'partition', 'get', 'size']).decode('utf-8').split('\n')

def get_disk_partition_description():
    return check_output(['wmic', 'partition', 'get', 'description']).decode('utf-8').split('\n')

def get_disk_partition_deviceid():
    return check_output(['wmic', 'partition', 'get', 'deviceid']).decode('utf-8').split('\n')

def get_disk_partition_index():
    return check_output(['wmic', 'partition', 'get', 'index']).decode('utf-8').split('\n')

def get_disk_partition_type():
    return check_output(['wmic', 'partition', 'get', 'type']).decode('utf-8').split('\n')

def get_graphics_card():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'name']).decode('utf-8').split('\n')

def get_graphics_card_name():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'name']).decode('utf-8').split('\n')

def get_graphics_card_driver():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'driverversion']).decode('utf-8').split('\n')

def get_graphics_card_status():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'status']).decode('utf-8').split('\n')

def get_graphics_card_manufacturer():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'manufacturer']).decode('utf-8').split('\n')

def get_graphics_card_deviceid():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'deviceid']).decode('utf-8').split('\n')

def get_graphics_card_index():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'index']).decode('utf-8').split('\n')

def get_graphics_card_ram():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'adapterram']).decode('utf-8').split('\n')

def get_graphics_card_currentresolution():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'currentresolution']).decode('utf-8').split('\n')

def get_graphics_card_maxresolution():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'maxresolution']).decode('utf-8').split('\n')

def get_graphics_card_currentverticalresolution():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'currentverticalresolution']).decode('utf-8').split('\n')

def get_graphics_card_maxverticalresolution():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'maxverticalresolution']).decode('utf-8').split('\n')

def get_graphics_card_currenthorizontalresolution():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'currenthorizontalresolution']).decode('utf-8').split('\n')

def get_graphics_card_maxhorizontalresolution():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'maxhorizontalresolution']).decode('utf-8').split('\n')

def get_graphics_card_currentrefreshrate():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'currentrefreshrate']).decode('utf-8').split('\n')

def get_graphics_card_maxrefreshrate():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'maxrefreshrate']).decode('utf-8').split('\n')

def get_graphics_card_currentbitsperpixel():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'currentbitsperpixel']).decode('utf-8').split('\n')

def get_graphics_card_maxbitsperpixel():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'maxbitsperpixel']).decode('utf-8').split('\n')

def get_graphics_card_currentnumberofcolors():
    return check_output(['wmic', 'path', 'win32_VideoController', 'get', 'currentnumberofcolors']).decode('utf-8').split('\n')

def audio_devices():
    return check_output(['wmic', 'path', 'win32_sounddevice', 'get', 'name']).decode('utf-8').split('\n')

def audio_devices_name():
    return check_output(['wmic', 'path', 'win32_sounddevice', 'get', 'name']).decode('utf-8').split('\n')

def audio_devices_manufacturer():
    return check_output(['wmic', 'path', 'win32_sounddevice', 'get', 'manufacturer']).decode('utf-8').split('\n')

def audio_devices_driver():
    return check_output(['wmic', 'path', 'win32_sounddevice', 'get', 'driverversion']).decode('utf-8').split('\n')

def audio_devices_status():
    return check_output(['wmic', 'path', 'win32_sounddevice', 'get', 'status']).decode('utf-8').split('\n')

def audio_devices_deviceid():
    return check_output(['wmic', 'path', 'win32_sounddevice', 'get', 'deviceid']).decode('utf-8').split('\n')

def audio_devices_index():
    return check_output(['wmic', 'path', 'win32_sounddevice', 'get', 'index']).decode('utf-8').split('\n')

def audio_devices_systemname():
    return check_output(['wmic', 'path', 'win32_sounddevice', 'get', 'systemname']).decode('utf-8').split('\n')




def main():
    get_wifi_passwords()
             
    
if __name__ == '__main__':
    main()
