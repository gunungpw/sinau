import psutil

with open("DiskInfo.ini", "w") as f:
    partition = psutil.disk_partitions()

    disk_mounpoint: list[str] = []

    for part in partition:
        disk_mounpoint.append(part.mountpoint)

    for mountpoint in disk_mounpoint:
        disk_usage = psutil.disk_usage(f"{mountpoint}")
        total, used, free, percent = disk_usage
        f.writelines(
            f"Disk mountpoint: {mountpoint}\n"
            f"Total: {total // (2**30)} GB\n"
            f"Used: {used // (2**30)} GB\n"
            f"Free: {free // (2**30)} GB\n"
        )
