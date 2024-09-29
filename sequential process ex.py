#sequential process
import time
def calc_sum_square(nums):
    result = 0
    for num in nums:
         result = result+num*num
        time.sleep(2)
    return result

def calc_sum_cube(nums):
    result = 0
    for num in nums:
        result = result+num*num*num
        time.sleep(1)
    return result

if __name__ == "__main__":
    start = datetime.datetime.now()
    nums = [1,2,3,4]
    result = calc_sum_square(nums)
    result = result+calc_sum_cube(nums)
    end = datetime.datetime.now()
    print(f'input value is {nums} and result is {result} and time elapsed is {end-start}')