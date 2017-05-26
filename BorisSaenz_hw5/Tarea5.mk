all: Resultados_hw5.pdf clean

Resultados_hw5.pdf: canal_ionico.c
	wget https://raw.githubusercontent.com/ClarkGuilty/2017/master/metodos/tareas/datosTarea5/Canal_ionico.txt
	wget https://raw.githubusercontent.com/ClarkGuilty/2017/master/metodos/tareas/datosTarea5/Canal_ionico1.txt
	wget https://raw.githubusercontent.com/ClarkGuilty/2017/master/metodos/tareas/datosTarea5/CircuitoRC.txt
	cc -o canal_ionico.o canal_ionico.c -lm
	-./canal_ionico.o
	python plots_canal_ionico.py
	python circuitoRC.py
	pdflatex Resultados_hw5.tex

clean: 
	-rm -f arch1.txt arch2.txt fig1.png fig2.png his1.png his2.png pru.png Vr.png Vc.png hC.png RrRc.png Rqt.png hR.png resultados.txt Canal_ionico.txt Canal_ionico1.txt CircuitoRC.txt Resultados_hw5.out canal_ionico.o Resultados_hw5.aux Resultados_hw5.log 
