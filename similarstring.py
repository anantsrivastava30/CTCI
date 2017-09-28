import time


def similarstring():
    x = int(input())
    if x < 1 or x > 5000:
        return "Invalid Testcase"
    y = []
    out = []
    for i in range(x):
        temp = int(input())
        if temp < 1 or temp > 5000:
            return "Invalid Testcase"
        y.append(temp)
        if y[i] == 1:
            sum = 26
            out.append(sum % 1000000007)
        else:
            sum = 0
            sum += (26*(1 - fast_power(26,y[i])))/(1-26)
            sum += 26*y[i]*(y[i] - 1)
            out.append(sum % 1000000007)
    for i in out:
        print(i)


def fast_power(a,n):
    result = 1
    value = a
    power = n
    while power > 0:
        if power % 2 == 1:
            result = result * value
        value = value * value
        power = int(power/2)
    return result


start_time = time.time()

def main():
    similarstring()

if __name__ == "__main__":
    main()
print("--- %s seconds ---" % (time.time() - start_time))
