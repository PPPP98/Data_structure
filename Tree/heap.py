def _sift_down(heap: list, start, end):
    root = start
    while True:
        child = 2 * root + 1  # 왼쪽 자식 idx
        if child > end:
            break  # 자식이 없으면 종료
        if child + 1 <= end and heap[child + 1] < heap[child]:
            child += 1
        if heap[root] > heap[child]:
            heap[root], heap[child] = heap[child], heap[root]
            root = child
        else:
            break


def _sift_up(heap: list, pos):
    child = pos
    while child > 0:
        parent = (child - 1) // 2
        if heap[child] < heap[parent]:
            heap[child], heap[parent] = heap[parent], heap[child]
            child = parent
        else:
            break


def heapify(heap: list):
    n = len(heap)
    for start in range((n // 2) - 1, -1, -1):
        _sift_down(heap, start, n - 1)


def heappush(heap: list, item):
    heap.append(item)
    _sift_up(heap, len(heap) - 1)


def heappop(heap: list):
    if not heap:
        raise IndexError("empty")

    last_item = heap.pop()
    if heap:
        return_item = heap[0]
        heap[0] = last_item
        _sift_down(heap, 0, len(heap) - 1)
        return return_item
    return last_item


def heappushpop(heap: list, item):
    if heap and heap[0] < item:
        item, heap[0] = heap[0], item
        _sift_down(heap, 0, len(heap) - 1)
        return item
    else:
        return item


def heapreplace(heap: list, item):
    if not heap:
        raise IndexError("empty")
    return_item = heap[0]
    heap[0] = item
    _sift_down(heap, 0, len(heap) - 1)
    return return_item


def nsmallest(n, iterable, key=None):
    """
    iterable에서 가장 작은 n개의 항목을 리스트로 반환합니다.
    """
    return sorted(iterable, key=key)[:n]


def nlargest(n, iterable, key=None):
    """
    iterable에서 가장 큰 n개의 항목을 리스트로 반환합니다.
    """
    return sorted(iterable, key=key, reverse=True)[:n]


# 먼저 reverse 정렬을 지원하기 위한 내부 래퍼 클래스를 정의합니다.
class _ReverseKey:
    """
    reverse 정렬을 위해 키의 비교 방향을 반전시키는 래퍼 클래스.
    """

    def __init__(self, obj):
        self.obj = obj

    def __lt__(self, other):
        return self.obj > other.obj

    def __gt__(self, other):
        return self.obj < other.obj

    def __eq__(self, other):
        return self.obj == other.obj

    def __le__(self, other):
        return self.obj >= other.obj

    def __ge__(self, other):
        return self.obj <= other.obj

    def __ne__(self, other):
        return self.obj != other.obj


def merge(*iterables, key=None, reverse=False):
    """
    여러 개의 정렬된 iterable을 하나의 정렬된 iterator로 병합합니다.

    매개변수:
      - key: 정렬 기준이 되는 함수 (기본값: None)
      - reverse: 정렬 순서를 반전할지 여부 (기본값: False)

    힙에 각 iterable의 첫 요소를 (정렬 기준, tie-breaker, 값, iterator) 튜플 형태로 넣어두고,
    힙에서 순차적으로 최소(또는 reverse일 경우 최대) 값을 pop하며 해당 iterator에서 다음 값을 넣습니다.
    """
    heap = []
    counter = 0
    # 각 iterable의 첫 요소를 힙에 추가
    for it in iterables:
        it = iter(it)
        try:
            first = next(it)
        except StopIteration:
            continue  # 빈 iterable은 건너뜀
        sort_val = key(first) if key is not None else first
        if reverse:
            sort_val = _ReverseKey(sort_val)
        heappush(heap, (sort_val, counter, first, it))
        counter += 1

    # 힙이 빌 때까지 가장 작은(또는 reverse인 경우 가장 큰) 항목을 pop하며 병합
    while heap:
        sort_val, _, value, it = heappop(heap)
        yield value
        try:
            next_value = next(it)
        except StopIteration:
            continue
        next_sort_val = key(next_value) if key is not None else next_value
        if reverse:
            next_sort_val = _ReverseKey(next_sort_val)
        heappush(heap, (next_sort_val, counter, next_value, it))
        counter += 1


if __name__ == "__main__":
    # 테스트 1: heapify, heappush, heappop, heappushpop, heapreplace
    print("----- Heap Functions Test -----")
    test_heap = [7, 2, 6, 3, 9, 1, 4]
    print("Original list:", test_heap)

    # heapify로 최소 힙으로 변환
    heapify(test_heap)
    print("After heapify:", test_heap)

    # heappush: 0 추가
    heappush(test_heap, 0)
    print("After heappush(0):", test_heap)

    # heappop: 최소값 제거
    popped = heappop(test_heap)
    print("heappop() returns:", popped)
    print("After heappop:", test_heap)

    # heappushpop: 5 삽입 후 최소값 제거
    pushpop_value = heappushpop(test_heap, 5)
    print("heappushpop(5) returns:", pushpop_value)
    print("After heappushpop:", test_heap)

    # heapreplace: 루트를 제거하고 8을 삽입
    replaced_value = heapreplace(test_heap, 8)
    print("heapreplace(8) returns:", replaced_value)
    print("After heapreplace:", test_heap)

    # 테스트 2: nsmallest와 nlargest
    print("\n----- nsmallest & nlargest Test -----")
    data = [5, 3, 8, 6, 2, 7, 1, 9, 4]
    print("Data:", data)
    print("nsmallest(3):", nsmallest(3, data))
    print("nlargest(3):", nlargest(3, data))

    # 테스트 3: merge
    print("\n----- Merge Test -----")
    sorted_list1 = [1, 4, 7, 10]
    sorted_list2 = [2, 5, 8, 11]
    sorted_list3 = [3, 6, 9, 12]
    print("Sorted lists:")
    print("List 1:", sorted_list1)
    print("List 2:", sorted_list2)
    print("List 3:", sorted_list3)

    merged_iter = merge(sorted_list1, sorted_list2, sorted_list3)
    merged_result = list(merged_iter)
    print("Merged result:", merged_result)
