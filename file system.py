import os
from pyprnt import prnt

#물리 드라이브를 읽기전용 및 이진모드로 연다.
drive = os.open("\\\\.\\PhysicalDrive1", os.O_RDONLY | os.O_BINARY)
#MBR 파티션 테이블 정보 불러오기
def get_mbr(drive_handle):
    mbr = []

    # Partition Table 영역을 읽어서
    # 저장해보자. Partition table은 446bytes
    # 뒤에 16bytes 씩 저장되어 있음
    # 최대 4개의 파티션 테이블이 있음

    #드라이브의 6번 바이트로 커서를 움직임. SEEK_SET은 시작에서 0만큼 움직인 것을 뜻함
    os.lseek(drive_handle, 0, os.SEEK_SET)
    # 드라이브의 0번 바이트에서 512바이트 만큼의 데이터를 읽음
    raw_data = os.read(drive_handle, 512)

    index = 446
    while index < 510:
        partition_data = raw_data[index: index + 16]
        index += 16

        if partition_data[4] == 0x00:
            continue

        mbr.append({
            "boot flag": partition_data[0],
            "Chs start": partition_data[1:4],
            "part type": partition_data[4],
            "Chs end": partition_data[5:8],
            "LBA start": int.from_bytes(partition_data[8:12], 'little'),
            "Size in sector": int.from_bytes(partition_data[12:18], 'little')
        })

    return mbr

def get_vbr(drive_handle, lba_start):
    vbr = {}

    # 드라이브 커서를 vbr 섹터로 이동함
    os.lseek(drive_handle, lba_start * 512, os.SEEK_SET)


    # vbr 섹터를 읽어옴.
    raw_data = os.read(drive_handle, 512)

    # TODO: 필요한 정보들을 dictionary 형식으로 정리
    # vbr["???"] = "어떤 값"
    vbr["bytes per sector"] = int.from_bytes(raw_data[11:13], "little")
    vbr["cluster per sector"] = raw_data[13]
    vbr["reserved sector"] = int.from_bytes(raw_data[14:16], "little")
    vbr["number of fat"] = raw_data[16]
    vbr["hidden sector"] = int.from_bytes(raw_data[28:32], "little")
    vbr["total sector 32"] = int.from_bytes(raw_data[32:36], "little")
    vbr["fat size 32"] = int.from_bytes(raw_data[36:40], "little")
    vbr["root directory cluster"] = int.from_bytes(raw_data[44:48], "little")
    vbr["file system info"] = int.from_bytes(raw_data[48:50], "little")

    return vbr

def get_fsinfo(drive_handle, fsinfo_sector):
    fsinfo = {}

    os.lseek(drive_handle, fsinfo_sector * 512, os.SEEK_SET)
    raw_data = os.read(drive_handle, 512)

    fsinfo["number of free clusters"] = int.from_bytes(raw_data[488:492], 'little')
    fsinfo["next free cluster"] = int.from_bytes(raw_data[492:496], 'little')


    return fsinfo

def get_rootdir_entrty(drive_handle, rootdir_sector):
    entry = []

    os.lseek(drive_handle, rootdir_sector * 512, os.SEEK_SET)
    raw_data = os.read(drive_handle, 512)
    index = 0
    while index < 512:
        raw_entry = raw_data[index:index + 32]
        index += 32

        # 파일이 더이상 없음
        if raw_entry[0] == 0x00:
            break
        # 삭제된 파일임
        if raw_entry[0] == 0xE5:
            continue
        # LFN 엔트리임
        if raw_entry[11] == 0x0F:
            continue

        entry.append({
            "name": str(raw_entry[0:8], encoding="ascii"),
            "extension": str(raw_entry[8:11], encoding="ascii"),
            "attr": raw_entry[11]
        })

    return entry
# mbr 정보를 가져옴
mbr = get_mbr(drive)
prnt(mbr)

# vbr 정보를 가져옴
vbr = get_vbr(drive, mbr[0]["LBA start"])
prnt(vbr)

# fsinfo 정보를 가져옴
fsinfo = get_fsinfo(drive, vbr["hidden sector"] + vbr["file system info"])
prnt(fsinfo)

rootdir_entrty = get_rootdir_entrty(drive,
     vbr["hidden sector"] + vbr["reserved sector"]
     + vbr["fat size 32"] * vbr["number of fat"])

prnt(rootdir_entrty)