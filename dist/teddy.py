#!/usr/bin/env python
import click
import os
import sys
from shutil import copyfile


@click.command()
@click.argument('filename', type=click.Path(exists=True))
def handler(filename):
    # click.echo(click.format_filename(filename))

    os_slash = "/"
    if os.name == 'nt':
        os_slash = "\\"
    path = os.getcwd() + os_slash
    path += click.format_filename(filename)
    sorted_path = path + " Sorted"
    if os.path.exists(sorted_path):
        click.echo(click.style("Error", fg="red") + ": Already sorted")
        sys.exit(0)

    os.mkdir(sorted_path)
    sorted_path += os_slash

    path += os_slash
    print(path)

    list_dir = os.listdir(path)
    sort = bubbleSort(list_dir)
    counter = 0
    for org in sort:
        for filename in os.listdir(path):
            if org == filename:
                dst = str(counter + 1) + "--)" + filename
                src = path + filename
                dst = sorted_path + dst
                copyfile(src, dst)
                counter += 1
                break
    click.echo(click.style("Info", fg="green") + ": Sorted Successfully")

def bubbleSort(arr):
    array = list(arr)
    for i in range(0, len(arr)):
        arr[i] = arr[i][-12:-4]

    # for i in array :
    #     print(i)
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return array


# for arg in sys.argv:
# print(arg)
# print(os.name)
# print(os.getcwd())

# directory = os.getcwd()
# directory += "/HW"
# directory += arg[0]
# print(directory)

if __name__ == '__main__':
    handler()
