#include <stdio.h>
#include <stdlib.h>
// N haman anazeye matis asat
#define N 9
//braye print kardn
int isSafe(int soudoko[N][N], int i, int j, int num)                              
{
    //check kardn satr
    for (int x = 0; x < 9; x++)
        if (soudoko[i][x] == num)
        {
        	 return 0;
		}
           
    //check kardan soton
    for (int x = 0; x < 9; x++)
        if (soudoko[x][j] == num)
        {
        	return 0;
		}
    //chek kardn 3*3
    for (int p = 0; p < 3; p++)
	     for (int q = 0; q < 3; q++)
	     	 if (soudoko[p + (i - i % 3)][q +(j - j % 3)] == num)
			  	    return 0;
			  
	
    return 1;
}
int solveSuduko(int soudoko[N][N], int i, int j)
{
    if (i == 8 && j == 9)
    {
    	//residan be tah
    	return 1;
	}
    if (j==9)
    {
    	//bro satr badi
        i++;
        //az ebteda satr shro kon
        j = 0;
    }
    //agar khali nist
    if (soudoko[i][j] > 0)
    {
    	//boro khane badi ro baresi kon
    	return solveSuduko(soudoko, i, j + 1);
 
	}
    //peyde kardn adad monaseb eyn 1 ta 9
    for (int rightn = 1; rightn <= 9; rightn++)
    {
    	//adad monaseb ast
        if (isSafe(soudoko, i, j, rightn)==1)
        {
        	//gharar dadn add jadid 
            soudoko[i][j] = rightn;
            if (solveSuduko(soudoko, i, j + 1)==1)
            {
            	   return 1;
			}   
        }
        soudoko[i][j] = 0;
    }
    return 0;
}
 
int main()
{
    int soudoko[N][N] = {0};
    for(int i=0;i<9;i++)
    {
    	for(int j=0;j<9;j++)
    	{
    		scanf("%d ",&soudoko[i][j]);
		}
	}
    if (solveSuduko(soudoko, 0, 0)==1)
        {
        	  for (int i = 0; i < 9; i++)
      {
         for (int j = 0; j < 9; j++)
         {
         	 printf("%d ",soudoko[i][j]);
		 }
         printf("\n");
      }
		}
    return 0;    

}
