#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include<time.h>


FILE *can;
FILE *can1;
double a;
double b;
int i;
int j;
int t = 0;
double c = 0;
double d = 0;
double var;
double x = 0.0;
double y = 8;
double x2 = 0;
double y2 = 0;
double esx[100];
double esy[100];
double xwh = 0;
double ywh = 0;
double radio(double x0, double y0);
void actualiza();
void suma(double D);
//double xwh2 = 0;
//double ywh2 = 0;
//usar solo un xwh o modificar el actualizador 

//hacer todod en el main

//afuera del main hacer metodo que me de radio, actualice y y sume pequeños

//2 while dos veces, uno para alpha

//cerrar text1 antes de iniciar 3 while

int main(void)
{
   	srand((unsigned) time(NULL));
   	
    FILE *text1=fopen("arch1.txt","w+");   	
    can=fopen("Canal_ionico.txt", "r");
    
    FILE *text2=fopen("arch2.txt","w+"); 
can1=fopen("Canal_ionico1.txt", "r");
    
    while(    fscanf(can, "%lf\n", &a) == 1)
    {
    esy[t/2] = a;
    t = t + 1;
    if((t % 2) == 1)
      { 
                esx[t/2] = a;
      }
    }
          
    int num = 200000;
	i = 0;
	
	
	
    while(i<num)
    {
          fprintf(text1, "%f %f\n", x, y);
          suma(0.3);
          double alpha = radio(xwh,ywh)/radio(x,y) ;
            if(alpha >1)
	    {
             x = xwh;
             y = ywh;
             x2 = x;
             y2 = y;
            }
            else
	    {
                 var = (double)rand()/RAND_MAX;
                 if(var>alpha)
		 {
                  x = xwh;
                  y = ywh;
                 }
            }
	i = i+1;
     }

//pasar datos a python

	FILE *out=fopen("resultados.txt","w+");    
 fprintf(out,"%f %f %f\n", xwh,ywh, radio(xwh,ywh));			
          
fclose(can);
fclose(text1);





    while(    fscanf(can1, "%lf\n", &a) == 1)
    {
    esy[t/2] = a;
    t = t + 1;
    if((t % 2) == 1)
        { 
          esx[t/2] = a;
        }
    }
          
    i = 0;
    while(i<num)
    {
          fprintf(text2, "%f %f\n", x, y);
          suma(0.3);
          double alpha = radio(xwh,ywh)/radio(x,y) ;
            if(alpha >1)
	    {
             x = xwh;
              y = ywh;
              x2 = x;
              y2 = y;
            }
            else
	      {
                 var = (double)rand()/RAND_MAX;
                 if(var>alpha)
		 {
                  x = xwh;
                  y = ywh;
                  }
              }
                 i++;
          }
    

fprintf(out,"%f %f %f\n", xwh,ywh, radio(xwh,ywh));			
fclose(can1);
fclose(out);
fclose(text2);



}




double radio(double x0, double y0)
{
       var = 0;
       double rta = (double) RAND_MAX;
       for(j = 0;j<t/2;j++)
          {
             var = sqrt( pow((x0-esx[j]),2) + pow((y0-esy[j]),2))-1;
             if(var<rta)
	      {
               rta = var;
              }
          }
       return rta;
       }

void actualiza()
{
     c= ((double)rand()/RAND_MAX)*2-1.0;
     d = ((double)rand()/RAND_MAX)*2-1.0;
     var = sqrt(c*c+d*d);
     c = c/var;
     d = d/var;
     
     }

void suma(double D)
{
     actualiza();

     xwh = x + D*c;
     ywh = y + D*d;
     
     }
     


       
