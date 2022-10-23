import base64
from uuid import UUID
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def str_index(str, index):
    return make_int(str[(index * 4):(index * 4)+4])

def plus_32bit(a1, a2):
    return (a1 + a2) & 0xffffffff

def make_int(str):
    count = 1
    result = 0
    for i in str:
        result += int(i) * count
        count *= 256
    return result

def str_to_int(string, index, value):
    for i in range(index, index + 4):
        string[i] = value & 0xff
        value >>= 8

def __ROL4__(left, right):
    left &= 0xffffffff
    shift = left << right
    shift &= 0xffffffff
    src = left >> (32 - right)
    return shift | src

def sub_101578ee0(enc_value, result, len_enc_value, au = 0):
    array1 = [-1] * 43 + [0x3e] + [-1] * 3 + [0x3f, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3a, 0x3b, 0x3c, 0x3d] + [-1] * 7 + [n for n in range(26)] + [-1] * 6 + [n for n in range(26, 52)] + [-1] * 100
    array2 = [0, 0, 0]
    choosed_array = array1
    if au:
        choosed_array = array2
    counter, result_counter, last_value, now_point = 0, 0, 0, 0
    while(True):
        if now_point == len_enc_value:
            break
        now_value = choosed_array[ord((enc_value[now_point]))]
        if now_value == -1:
            now_value = last_value
            
        elif counter == 0:
            counter = 1
                
        elif counter == 1:
            counter = 2
            if result_counter < len_enc_value:
                result_counter += 1
                result += [(((now_value >> 4) & 3) + last_value * 4) & 0xff]
            
        elif counter == 2:
            counter = 3
            if result_counter < len_enc_value:
                result_counter += 1
                result += [((16 * last_value) | (now_value >> 2) & 0xf) & 0xff]
            
        elif counter == 3:
            counter = 0
            if result_counter < len_enc_value:
                result_counter += 1
                result += [(now_value | (last_value << 6)) & 0xff]
            
        else:
            pass
        last_value = now_value
        now_point += 1
        
    return result_counter 

def sub_10155a720(string):
    return string + "1EBA5A37-581C-4f8b-AB8D-C9447867514B"

def sub_1013b7f10():
    return [0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef, 0xfe, 0xdc, 0xba, 0x98, 0x76, 0x54, 0x32, 0x10]
        
def sub_1013B7550(result, reform_username, name_len):
    result += [(8 * name_len) & 0xff, ((8 * name_len) & 0xff00) >> 8]
    result += [00] * 6
    count = 0
    for i in reform_username:
        count += 1
        result += [ord(i)]
    result += [0] * (64 - count)
    result += [name_len]
    
def sub_1013B76B0(total, name, a3):
    v4 = str_index(total, 3)
    v5 = str_index(total, 2)
    v6 = str_index(total, 0)
    v7 = str_index(total, 1)
    while True:
        v73 = a3
        v87 = str_index(name, 2)
        v8 = v7 + __ROL4__(str_index(name, 0) + v6 + (v4 ^ v7 & (v4 ^ v5)) - 680876936, 7)
        v81 = str_index(name, 1)
        v75 = str_index(name, 3)
        v9 = plus_32bit(v8, __ROL4__((v5 ^ v8 & (v5 ^ v7)) + v81 + v4 - 389564586, 12))
        v10 = plus_32bit(v9, __ROL4__((v7 ^ v9 & (v7 ^ v8)) + v87 + v5 + 606105819, 17))
        v84 = str_index(name, 4)
        v11 = plus_32bit(v10, __ROL4__((v8 ^ v10 & (v8 ^ v9)) + v75 + v7 - 1044525330, 22))
        v12 = str_index(name, 5)
        v13 = plus_32bit(v11, __ROL4__((v9 ^ v11 & (v9 ^ v10)) + v84 + v8 - 176418897, 7))
        v76 = str_index(name, 7)
        v14 = v13 + __ROL4__((v10 ^ v13 & (v10 ^ v11)) + v12 + v9 + 1200080426, 12)
        v80 = str_index(name, 6)
        v15 = v14 + __ROL4__((v11 ^ v14 & (v11 ^ v13)) + v80 + v10 - 1473231341, 17)
        v16 = v15 + __ROL4__((v13 ^ v15 & (v13 ^ v14)) + v76 + v11 - 45705983, 22)
        v85 = str_index(name, 8)
        v17 = v16 + __ROL4__((v14 ^ v16 & (v14 ^ v15)) + v85 + v13 + 1770035416, 7)
        v82 = str_index(name, 9)
        v18 = v17 + __ROL4__((v15 ^ v17 & (v15 ^ v16)) + v82 + v14 - 1958414417, 12)
        v78 = str_index(name, 10)
        v19 = v18 + __ROL4__((v16 ^ v18 & (v16 ^ v17)) + v78 + v15 - 42063, 17)
        v79 = str_index(name, 11)
        v20 = v19 + __ROL4__((v17 ^ v19 & (v17 ^ v18)) + v79 + v16 - 1990404162, 22)
        v83 = str_index(name, 12)
        v21 = v20 + __ROL4__((v18 ^ v20 & (v18 ^ v19)) + v83 + v17 + 1804603682, 7)
        v86 = str_index(name, 13)
        v22 = v21 + __ROL4__((v19 ^ v21 & (v19 ^ v20)) + v86 + v18 - 40341101, 12)
        v23 = str_index(name, 14)
        v24 = v22 + __ROL4__((v20 ^ v22 & (v20 ^ v21)) + v23 + v19 - 1502002290, 17)
        v77 = str_index(name, 15);
        v25 = v24 + __ROL4__((v21 ^ v24 & (v21 ^ v22)) + v77 + v20 + 1236535329, 22)
        v26 = v25 + __ROL4__((v24 ^ v22 & (v24 ^ v25)) + v81 + v21 - 165796510, 5)
        v27 = v26 + __ROL4__((v25 ^ v24 & (v25 ^ v26)) + v80 + v22 - 1069501632, 9)
        v28 = v27 + __ROL4__((v26 ^ v25 & (v26 ^ v27)) + v79 + v24 + 643717713, 14)
        v29 = v28 + __ROL4__((v27 ^ v26 & (v27 ^ v28)) + str_index(name, 0) + v25 - 373897302, 20)
        v30 = v29 + __ROL4__((v28 ^ v27 & (v28 ^ v29)) + v12 + v26 - 701558691, 5)
        v31 = v30 + __ROL4__((v29 ^ v28 & (v29 ^ v30)) + v78 + v27 + 38016083, 9)
        v32 = v31 + __ROL4__((v30 ^ v29 & (v30 ^ v31)) + v77 + v28 - 660478335, 14)
        v33 = v32 + __ROL4__((v31 ^ v30 & (v31 ^ v32)) + v84 + v29 - 405537848, 20)
        v34 = v33 + __ROL4__((v32 ^ v31 & (v32 ^ v33)) + v82 + v30 + 568446438, 5)
        v35 = v34 + __ROL4__((v33 ^ v32 & (v33 ^ v34)) + v23 + v31 - 1019803690, 9)
        v36 = v35 + __ROL4__((v34 ^ v33 & (v34 ^ v35)) + v75 + v32 - 187363961, 14)
        v37 = v36 + __ROL4__((v35 ^ v34 & (v35 ^ v36)) + v85 + v33 + 1163531501, 20)
        v38 = v37 + __ROL4__((v36 ^ v35 & (v36 ^ v37)) + v86 + v34 - 1444681467, 5)
        v39 = v38 + __ROL4__((v37 ^ v36 & (v37 ^ v38)) + v87 + v35 - 51403784, 9)
        v40 = v39 + __ROL4__((v38 ^ v37 & (v38 ^ v39)) + v76 + v36 + 1735328473, 14)
        v41 = v40 + __ROL4__((v39 ^ v38 & (v39 ^ v40)) + v83 + v37 - 1926607734, 20)
        v42 = v41 + __ROL4__((v41 ^ v39 ^ v40) + v12 + v38 - 378558, 4)
        v43 = v42 + __ROL4__((v42 ^ v40 ^ v41) + v85 + v39 - 2022574463, 11)
        v44 = v43 + __ROL4__((v43 ^ v41 ^ v42) + v79 + v40 + 1839030562, 16)
        v45 = v44 + __ROL4__((v44 ^ v42 ^ v43) + v23 + v41 - 35309556, 23)
        v46 = v45 + __ROL4__((v45 ^ v43 ^ v44) + v81 + v42 - 1530992060, 4)
        v47 = v46 + __ROL4__((v46 ^ v44 ^ v45) + v84 + v43 + 1272893353, 11)
        v48 = v47 + __ROL4__((v47 ^ v45 ^ v46) + v76 + v44 - 155497632, 16)
        v49 = v48 + __ROL4__((v48 ^ v46 ^ v47) + v78 + v45 - 1094730640, 23)
        v50 = v49 + __ROL4__((v49 ^ v47 ^ v48) + v86 + v46 + 681279174, 4)
        v51 = v50 + __ROL4__((v50 ^ v48 ^ v49) + str_index(name, 0) + v47 - 358537222, 11)
        v52 = v51 + __ROL4__((v51 ^ v49 ^ v50) + v75 + v48 - 722521979, 16)
        v53 = v52 + __ROL4__((v52 ^ v50 ^ v51) + v80 + v49 + 76029189, 23)
        v54 = v53 + __ROL4__((v53 ^ v51 ^ v52) + v82 + v50 - 640364487, 4)
        v55 = v54 + __ROL4__((v54 ^ v52 ^ v53) + v83 + v51 - 421815835, 11)
        v56 = v55 + __ROL4__((v55 ^ v53 ^ v54) + v77 + v52 + 530742520, 16)
        v57 = v56 + __ROL4__((v56 ^ v54 ^ v55) + v87 + v53 - 995338651, 23)
        v58 = v57 + __ROL4__((v56 ^ (v57 | ~v55)) + str_index(name, 0) + v54 - 198630844, 6);
        v59 = v58 + __ROL4__((v57 ^ (v58 | ~v56)) + v76 + v55 + 1126891415, 10)
        v60 = v59 + __ROL4__((v58 ^ (v59 | ~v57)) + v23 + v56 - 1416354905, 15)
        v61 = v60 + __ROL4__((v59 ^ (v60 | ~v58)) + v12 + v57 - 57434055, 21)
        v62 = v61 + __ROL4__((v60 ^ (v61 | ~v59)) + v83 + v58 + 1700485571, 6)
        v63 = v62 + __ROL4__((v61 ^ (v62 | ~v60)) + v75 + v59 - 1894986606, 10)
        v64 = v63 + __ROL4__((v62 ^ (v63 | ~v61)) + v78 + v60 - 1051523, 15)
        v65 = v64 + __ROL4__((v63 ^ (v64 | ~v62)) + v81 + v61 - 2054922799, 21)
        v66 = v65 + __ROL4__((v64 ^ (v65 | ~v63)) + v85 + v62 + 1873313359, 6)
        v67 = v66 + __ROL4__((v65 ^ (v66 | ~v64)) + v77 + v63 - 30611744, 10)
        v68 = v67 + __ROL4__((v66 ^ (v67 | ~v65)) + v80 + v64 - 1560198380, 15)
        v69 = v68 + __ROL4__((v67 ^ (v68 | ~v66)) + v86 + v65 + 1309151649, 21)
        v70 = v69 + __ROL4__((v68 ^ (v69 | ~v67)) + v84 + v66 - 145523070, 6)
        v71 = v70 + __ROL4__((v69 ^ (v70 | ~v68)) + v79 + v67 - 1120210379, 10)
        v72 = v71 + __ROL4__((v70 ^ (v71 | ~v69)) + v87 + v68 + 718787259, 15)
        v7 = __ROL4__((v71 ^ (v72 | ~v70)) + v82 + v69 - 343485551, 21) + v72 + str_index(total, 1)
        v6 = str_index(total, 0) + v70
        v5 = str_index(total, 2) + v72
        v4 = str_index(total, 3) + v71
        str_to_int(total, 0, v6 & 0xffffffff)
        str_to_int(total, 4, v7 & 0xffffffff)
        str_to_int(total, 8, v5 & 0xffffffff)
        str_to_int(total, 12, v4 & 0xffffffff)
        a3 = v73 - 1
        if v73 == 1:
          break
      
def sub_1013B7E50(second_reform, first_reform):
    first_reform[24 + int(first_reform[88])] = 0x80
    str_to_int(first_reform, 80, str_index(first_reform, 4))
    sub_1013B76B0(first_reform, first_reform[24:], 1)
    for i in range(16):
        second_reform.append(first_reform[i])
    
    
def sub_1013B7F90(user_name_plus_pin, length, result):
    first_reform = sub_1013b7f10()
    sub_1013B7550(first_reform, user_name_plus_pin, length)
    sub_1013B7E50(result, first_reform)
    return result
            
if __name__ == "__main__":
    user_name = input()
    user_name_plus_pin = sub_10155a720(user_name)
    result = []
    enc_result = []
    lrst_value = input()
    sub_1013B7F90(user_name_plus_pin, len(user_name_plus_pin), result)
    sub_101578ee0(lrst_value, enc_result, len(lrst_value))
    key = bytes()
    for i in result:
        key += i.to_bytes(1, 'little')
    cipher_text = bytes()
    for i in enc_result:
        cipher_text += i.to_bytes(1, 'little')
    iv = UUID("1EBA5A38-581C-4f8b-AB8D-C94478675142").bytes
    cipher = AES.new(key, AES.MODE_ECB)
    plain_text = cipher.decrypt(cipher_text)
    for i in plain_text:
        print(chr(i), end = '')
