#ifndef PERSON_H
#define PERSON_H

#include <iostream>
#include <string>
#include <sstream>

class Person {
private:
    int age;
public:
    std::string first_name;
    std::string last_name;

    Person(std::string fname, std::string lname, int a) {
        first_name = fname;
        last_name = lname;
        age = a;
    }

    int getAge() {
        return age;
    }

    void ageUp() {
        age += 1;
    }

    std::string getFullname() {
        return first_name + " " + last_name;
    }

    void printFullname() {
        std::cout << first_name << " " << last_name << std::endl;
    }
};

#endif
