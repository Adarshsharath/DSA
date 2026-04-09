//I have used string matching concept here thats it it was an easy question

int strStr(char* haystack, char* needle) {
    int count = 0;
    int scount = 0;
    for(int i = 0;haystack[i]!='\0';i++){
        count++;
    }
    for(int i = 0;needle[i]!='\0';i++){
        scount++;
    }
    for(int i = 0;i<=(count - scount);i++){
        int j = 0;
        int k =i;
        while(j<scount && haystack[k]==needle[j]){
            j++;
            k++;
        }
        if (j == scount){
            return (k-scount);
        }
    }
    return -1;
}