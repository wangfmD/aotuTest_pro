#!/usr/bin/python2.7
#coding=utf8
r'''
Fuction: 
Version: 1.0.0
Created: Tuyj
Created date:2015/1/19
'''
#thread stack size,min=32k
default_mini_thread_stack_size   = 512000 #512k
default_small_thread_stack_size  = 1024000 #1M
default_normal_thread_stack_size = 2048000 #2M
default_large_thread_stack_size  = 4096000 #4M
default_linux_sys_thread_stack_size = 8192000 #8M
max_multitask_inv = 0.5
_local_debug_mode = True

pre_video_size_map = {
    "qvga"  :("320x240",   320,  240), 
    "vga"   :("640x480",   640,  480), 
    "svga"  :("800x600",   800,  600), 
    "xga"   :("1024x768",  1024, 768), 
    "sxga"  :("1280x1024", 1280, 1024),
    "qcif"  :("176x144",   176,  144), 
    "cif"   :("352x288",   352,  288), 
    "4cif"  :("704x576",   704,  576), 
    "w228p" :("512x288",   512,  288), 
    "w448p" :("768x448",   768,  448), 
    "w576p" :("1024x576",  1024, 576), 
    "240p"  :("320x240",   320,  240), 
    "360p"  :("640x360",   640,  360), 
    "480p"  :("832x480",   832,  480), 
    "720p"  :("1280x720",  1280, 720), 
    "1080p" :("1920x1080", 1920, 1080),
    "N/A"   :("0x0",       0,    0)
}
def w_h2sizeStr(width, height):
    for sizestr,(dual,w,h) in pre_video_size_map.iteritems():
        if width == w and height == h:
            return sizestr
    return None

payload_map = {
    "H264"        : 109,
    "PCMU/8000/1" : 0,
    "PCMA/8000/1" : 8,
    "G722/16000/1": 9, 
    "ILBC/8000/1" : 102, 
    "ISAC/16000/1": 103, 
    "ISAC/32000/1": 104, 
    "ISAC/48000/1": 105,
    "OPUS/48000/1": 106,
    "PCMU/8000/2" : 110,
    "PCMA/8000/2" : 118,
    "G722/16000/2": 119,
    "OPUS/48000/2": 120
}

audio_channel_str = ['none', 'mono', 'stereo']

profile_name_map = {
    'cbase'     : 'CB' ,
    'baseline'  : 'B'  ,
    'main'      : 'M'  ,
    'extended'  : 'E'  ,
    'high'      : 'H'  ,
    'high10'    : 'H10',
    'high422'   : 'H42',
    'high444'   : 'H44',
}

