def runningSum(nums):
    """Дан массив nums. Мы определяем текущую сумму массива как
    runningSum[i] = sum(nums[0]…nums[i]).
    Вернуть текущую сумму nums.

    Хотя это не очень сложная задача, это хорошее введение в концепцию массива сумм префиксов . Массивы сумм префиксов имеют множество применений в более сложных алгоритмах и иногда могут помочь уменьшить временную сложность сложного решения на порядок.
    В массиве сумм префиксов мы создадим повторяющийся массив, который содержит текущую сумму элементов от 0 до i нашего исходного массива ( nums ) для каждого индекса i нашего массива сумм префиксов ( ans ). ( Примечание : мы можем снизить сложность пространства , используя подход на месте с nums напрямую и преобразовав его в собственный массив сумм префиксов, если нет веских причин избегать изменения аргумента функции.)
    Поскольку нам нужно будет опираться на предыдущую промежуточную сумму, мы должны начать нашу итерацию с i = 1 и скопировать первый элемент из nums в ans . Затем мы просто перебираем числа и добавляем каждый элемент ( nums [i] ) к предыдущему промежуточному итогу ( ans[i-1] ), чтобы создать новый промежуточный итог ( ans[i] ).
    Когда мы закончим, мы можем вернуть ans. Временная сложность: O(N), где N — длина чисел

    Пространственная сложность: O(N) для нашего массива текущей суммы или O(1) с подходом на месте"""

    ans = [0] * len(nums)  # init answer array
    ans[0] = nums[0]  # ans[0] element
    for i in range(1, len(nums)):
        ans[i] = ans[i - 1] + nums[i]
    return ans


def pivotIndex(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return ""


def finalValueAfterOperations(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    x = 0
    for i in operations:
        if str(i).__contains__("+"):
            x += 1
        else:
            x -= 1
    return x


def mostWordsFound(self, sentences):
    """
    :type sentences: List[str]
    :rtype: int
    """
    x = 0
    for i in sentences:
        y = str(i).split(" ").__len__()
        if x < y:
            x = y
    return x
