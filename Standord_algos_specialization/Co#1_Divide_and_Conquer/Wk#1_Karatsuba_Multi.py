def K_Multiply(x, y):
    x_str = str(x)
    y_str = str(y)
    padded = False
    if len(x_str) > len(y_str):
        padded = True
        y_str += "0"
    if len(y_str) > len(x_str):
        padded = True
        x_str += "0"
    if (len(x_str) == 1) and (len(y_str) == 1):
        return x * y
    else:
        mid_x = int(len(x_str) / 2)
        mid_y = int(len(y_str) / 2)
        a = int(x_str[:mid_x])
        b = int(x_str[mid_x:])
        c = int(y_str[:mid_y])
        d = int(y_str[mid_y:])

        step1 = K_Multiply(a, c)
        step2 = K_Multiply(b, d)
        step3 = K_Multiply((a + b), (c + d))
        step4 = step3 - step2 - step1
        result = (
            (step1 * 10 ** (2 * len(x_str[mid_x:])))
            + (step2)
            + (step4 * 10 ** (len(x_str[mid_x:])))
        )
        if padded:
            if result != 0:
                result_str = str(result)
                result_fix = int(result_str[:-1])
                return result_fix
        return result


# """
print(
    K_Multiply(
        3141592653589793238462643383279502884197169399375105820974944592,
        2718281828459045235360287471352662497757247093699959574966967627,
    )
)
# """
