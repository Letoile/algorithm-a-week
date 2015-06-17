def prod_tree(left, right):
    if left > right:
        return 1
    if left == right:
        return left
    if right - left == 1:
        return left * right
    mediana = (right + left) // 2
    return prod_tree(left, mediana) * prod_tree(mediana + 1, right)


def fact_tree(number):
    if number < 0:
        return 0
    if number == 0:
        return 1
    if number == 1 or number == 2:
        return number
    return prod_tree(2,number)
