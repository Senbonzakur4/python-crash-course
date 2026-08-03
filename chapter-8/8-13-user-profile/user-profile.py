# 8.13 User Profile

def build_profile(first, last, **user_info):
    
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user = build_profile('Oziel', 'Velazquez', age=27,location='Mexico', 
                     field='Software Development')

print(f"\n{user}\n")
