CXXFLAGS+=-Wall -std=c++14

all: Makefile alloc

alloc: allocator.o
	$(CXX) $(CXXFLAGS) allocator.o -o alloc

MyAllocator.o: allocator.cpp test.h
	$(CXX) -c $(CXXFLAGS) allocator.cpp

clean:
	rm -rf *.o alloc
