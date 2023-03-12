price_list = [32100, 32150, 32000, 32500]

for num, result in enumerate(price_list):
    print(num, result)


    
    
# 위와 같은 출력을 위해서는 for 루프와 enumerate() 함수를 사용하면 됩니다. enumerate() 함수는 리스트 요소의 인덱스와 값을 순서쌍(tuple) 형태로 반환하므로, 이를 이용하여 인접한 두 요소씩 출력할 수 있습니다. 다음은 예제 코드입니다.

my_list = ["가", "나", "다", "라"]

for i, item in enumerate(my_list[:-1]):
    print(item, my_list[i+1])
# 위 코드에서 enumerate() 함수를 이용하여 my_list의 인덱스와 값을 반환하면서, 리스트의 마지막 요소를 제외한 모든 요소에 대해 반복문을 실행합니다. 
# 이때, enumerate() 함수가 반환한 인덱스 i는 현재 요소의 인덱스를, item은 현재 요소의 값을 가리킵니다. 
# print() 함수를 이용하여 item과 그 다음 요소 my_list[i+1]를 출력하면 됩니다.

