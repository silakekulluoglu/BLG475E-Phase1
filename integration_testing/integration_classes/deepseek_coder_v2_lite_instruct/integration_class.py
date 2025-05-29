from typing import List

class TreeProcessor:

    def greatest_common_divisor(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def pluck(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []
        evens = list(filter(lambda x: x % 2 == 0, arr))
        if evens == []:
            return []
        return [min(evens), arr.index(min(evens))]

    def rescale_to_unit(self, numbers: List[float]) -> List[float]:
        min_number = min(numbers)
        max_number = max(numbers)
        return [(x - min_number) / (max_number - min_number) for x in numbers]

    def process_tree_branch(self, arr: List[int]) -> dict:

        plucked_node = self.pluck(arr)
        if not plucked_node:
            return {"plucked_node": [], "gcd": None, "rescaled_branch": []}

        gcd_result = self.greatest_common_divisor(plucked_node[0], plucked_node[1])

        rescaled_branch = self.rescale_to_unit([float(x) for x in arr])

        return {
            "plucked_node": plucked_node,
            "gcd": gcd_result,
            "rescaled_branch": rescaled_branch
        }


if __name__ == "__main__":
    processor = TreeProcessor()

    branch = [5, 0, 3, 0, 4, 2]

    result = processor.process_tree_branch(branch)
    print("Plucked Node:", result["plucked_node"])
    print("GCD of Plucked Node's Value and Index:", result["gcd"])
    print("Rescaled Branch Values:", result["rescaled_branch"])

