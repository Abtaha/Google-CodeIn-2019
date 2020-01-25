all:
	@g++ -o main main.cpp
	@./main
	@python3 plotter.py

dependencies:
	sudo apt-get install python3
	pip3 install matplotlib

clean:
	@rm -f Data.txt
	@rm -f main