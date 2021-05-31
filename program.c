int main()
{

    float a;
    double b;
    a = 1.1;
    int i, inc, j;
    i = 0;
    
    inc = 2;
    read j;
    while (i < j)
    {
        i = i + inc;
        a = a*i;
    }

    if (a > 10.0 && a == 0.1)
    {
        print(a + i);
    } else if (a < -1 || a == 0.0) 
    {
        print(a - i);
    }
}
