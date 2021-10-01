with open('binary.bin', 'wb') as f :
    byte_list = bytes([255,0,127]) #3바이트 데이터 11111111_00000000_01111111
    f.write(byte_list)