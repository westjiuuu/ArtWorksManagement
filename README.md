# 🎨미술작품 유지보수 시스템🛠️

우선순위 큐를 사용하여 미술 작품의 상태와 그에 따른 유지 보수 우선순위를 효율적으로 관리할 수 있습니다

## 기능

- 미술 작품의 액자 여부, 크기, 도구 사용 여부, 최근 작품 여부, 유명한 작가 여부 등 다양한 기준을 활용하여 작품의 우선순위를 정할 수 있습니다.
- 최소 힙(Min Heap)을 활용하여 우선순위 큐를 구현하고, 내림차순으로 정렬하여 우선순위가 높은(priority 값이 큰) 작품을 먼저 유지보수할 수 있습니다.
- 작품 추가 및 삭제 기능을 제공합니다.

## 사용법

1. 프로그램 실행 후 작품을 추가하거나 삭제할지 선택합니다.
2. 작품을 추가하려면 작품의 속성(액자 여부, 크기, 도구 사용 여부 등)을 입력합니다.
3. 작품을 삭제하려면 작품의 이름을 입력합니다.
4. 프로그램 종료 시 현재 우선순위에 따라 작품이 출력됩니다.

## 예시

```python
# Example Usage
maintenance = ArtworkMaintenance()

# Artwork 객체 생성 및 추가
artwork1 = Artwork("1", False, "Small", False, False, True, "유화", "low")
maintenance.add_artwork(artwork1)

# 콘솔 예시
작품을 추가하시겠습니까? (y/n): y
작품 이름: 해바라기 
액자가 있습니까? (True/False): True
크기 (Large/Medium/Small): Small
도구를 사용했습니까? (True/False): False
최근 작품입니까? (True/False): False
유명한 작가인가요? (True/False): True
재료: 유화 
복잡성 (VeryHigh/High/Medium/Low): Low
작품을 추가하시겠습니까? (y/n): n
작품을 삭제하시겠습니까? (y/n): n
Highest priority artwork: 1, Priority: 35
Highest priority artwork: 해바라기 , Priority: 25
