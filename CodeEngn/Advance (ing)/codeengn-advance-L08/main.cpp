#include <iostream>

unsigned int first(int val[]){
    int esi, edx = 0;

    for (int i = 0; i < 2; i++) {

        esi = val[i];
        esi = esi + edx;
        esi = esi * 0x772;
        edx = esi;
        edx = edx * esi;
        esi = esi + edx;
        esi = esi | esi;
        esi = esi * 0x474;
        esi = esi + esi;
        edx = esi;


    }
    return (edx & 0xffff0000) >> 16;
}

unsigned int second(int val[]){
    int edx = 0;
    int ebp = 0;

    for (int i = 1; i >= 0; i--) {
        edx = val[i] + 0x11;
        edx = edx - 5;
        edx = edx * 0x92;
        edx = edx + edx;
        edx = edx * 0x819;
        ebp = ebp + edx;
    }
    return (ebp & 0xfffff000) >> 12;
}

int main() {

    for (int i = 33; i < 134; ++i) {
        for (int j = 33; j < 134; ++j) {
            int value[2] = {i, j};
            unsigned int a = first(value);
            unsigned int b = second(value);

            if(a == 0x5D88 && b == 0x53B4){
                std::cout <<  char(i) << char(j) << std::endl;
            }
        }
    }

    return 0;
}