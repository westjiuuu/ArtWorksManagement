import heapq

class Artwork:
    def __init__(self, name, has_frame, size, used_tools, is_recent, is_famous_artist, material, complexity):
        self.name = name
        self.has_frame = has_frame
        self.size = size
        self.used_tools = used_tools
        self.is_recent = is_recent
        self.is_famous_artist = is_famous_artist
        self.material = material
        self.complexity = complexity
        self.priority = self.calculate_priority()

    def calculate_priority(self):
        priority = 0
        if self.has_frame:
            priority += 0
        else:
            priority += 10
        if self.size == "Large":
            priority += 10
        elif self.size == "Medium":
            priority += 5
        if self.used_tools:
            priority += 5
        if self.is_recent:
            priority += 0
        else:
            priority += 10
        if self.is_famous_artist:
            priority += 10
        if self.material == "유화":
            priority += 5
        if self.complexity == "VeryHigh":
            priority += 15
        elif self.complexity == "High":
            priority += 13
        elif self.complexity == "Medium":
            priority += 10
        elif self.complexity == "Low":
            priority += 5
        return priority

    def __lt__(self, other):
        return self.priority < other.priority

class ArtworkMaintenance:
    def __init__(self):
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        self.artworks = sorted(self.artworks, key=lambda x: x.priority, reverse=True)

    def remove_artwork(self, artwork_name):
        for i, artwork in enumerate(self.artworks):
            if artwork.name == artwork_name:
                del self.artworks[i]
                return True
        return False

    def get_highest_priority(self):
        if self.artworks:
            highest_priority_artwork = self.artworks.pop(0)
            return highest_priority_artwork
        else:
            return None

# Example Usage
maintenance = ArtworkMaintenance()
artworks = [
Artwork("1", False, "Small", False, False, True, "유화", "low"),
Artwork("2", False, "Small", False, False, True, "유화", "low"),
Artwork("3", False, "Small", True, True, True, "혼합", "VeryHigh"),
Artwork("4", False, "Large", False, False, True, "유화", "Medium"),
Artwork("5", False, "Small", True, True, True, "혼합", "VeryHigh"),
Artwork("6", False, "Medium", False, False, True, "유화", "Medium"),
Artwork("7", False, "Medium", True, False, True, "유화", "High"),
Artwork("8", False, "Small", True, False, True, "유화", "High"),
Artwork("9", False, "Small", True, False, True, "유화", "High"),
Artwork("10", False, "Medium", False, False, True, "유화", "Low"),
Artwork("11", False, "Medium", True, True, True, "혼합", "VeryHigh"),
Artwork("12", False, "Small", True, True, True, "혼합", "VeryHigh"),
Artwork("13", False, "Small", True, True, True, "혼합", "VeryHigh"),
Artwork("14", False, "Large", False, False, True, "유화", "High"),
Artwork("15", False, "Medium", True, False, True, "유화", "High"),
Artwork("16", False, "Small", False, False, True, "목탁", "Low"),
Artwork("17", False, "Large", True, True, True, "유화", "Medium"),
Artwork("18", False, "Large", True, True, True, "유화", "Medium"),
Artwork("19", True, "Small", False, False, True, "유화", "Low"),
Artwork("20", True, "Small", False, False, True, "유화", "Low"),
Artwork("21", False, "Small", False, False, True, "목탄", "Low"),
Artwork("22", False, "Small", False, False, True, "목탄", "Low"),
Artwork("23", False, "Small", True, True, True, "혼합", "VeryHigh"),
Artwork("24", False, "Small", True, True, True, "혼합", "VeryHigh"),
Artwork("25", True, "Small", False, False, True, "유화", "Low"),
Artwork("26", True, "Small", False, False, True, "유화", "Low"),
Artwork("27", True, "Small", False, False, True, "유화", "Low"),
Artwork("28", False, "Large", True, True, True, "혼합", "VeryHigh"),
Artwork("29", False, "Large", True, True, True, "혼합", "VeryHigh"),
Artwork("30", False, "Large", True, True, True, "혼합", "VeryHigh")
]

for artwork in artworks:
    maintenance.add_artwork(artwork)

while True:
    user_input = input("작품을 추가하시겠습니까? (y/n): ")
    if user_input.lower() == 'y':
        name = input("작품 이름: ")
        has_frame = input("액자가 있습니까? (True/False): ").lower() == 'true'
        size = input("크기 (Large/Medium/Small): ")
        used_tools = input("도구를 사용했습니까? (True/False): ").lower() == 'true'
        is_recent = input("최근 작품입니까? (True/False): ").lower() == 'true'
        is_famous_artist = input("유명한 작가인가요? (True/False): ").lower() == 'true'
        material = input("재료: ")
        complexity = input("복잡성 (VeryHigh/High/Medium/Low): ")

        artwork = Artwork(name, has_frame, size, used_tools, is_recent, is_famous_artist, material, complexity)
        maintenance.add_artwork(artwork)
    elif user_input.lower() == 'n':
        delete_input = input("작품을 삭제하시겠습니까? (y/n): ")
        if delete_input.lower() == 'y':
            artwork_name = input("삭제할 작품의 이름: ")
            if maintenance.remove_artwork(artwork_name):
                print(f"{artwork_name} 작품이 삭제되었습니다.")
            else:
                print(f"{artwork_name} 작품을 찾을 수 없습니다.")
        elif delete_input.lower() == 'n':
            highest_priority_artwork = maintenance.get_highest_priority()
            while highest_priority_artwork:
                print(f"Highest priority artwork: {highest_priority_artwork.name}, Priority: {highest_priority_artwork.priority}")
                highest_priority_artwork = maintenance.get_highest_priority()
            break
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")
    else:
        print("잘못된 입력입니다. 다시 시도해주세요.")