import threading
import datetime
import time

result = 0
def calc_sum_squares(nums):
    global result
    for num in nums:
        result = result + num*num
        time.sleep(2)


def calc_sum_cubes(nums):
    global result
    for num in nums:
        result = result+num*num*num
        time.sleep(1)


if __name__ == "__main__":
    start = datetime.datetime.now()
    nums = [1,2,3,4]
    thread1 = threading.Thread(target = calc_sum_squares,args = (nums,),)
    thread2 = threading.Thread(target = calc_sum_cubes, args = (nums,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    end = datetime.datetime.now()
    print(f'input :{nums} result = {result} and time taken is {end-start}')