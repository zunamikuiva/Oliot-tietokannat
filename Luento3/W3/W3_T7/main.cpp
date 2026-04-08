#include <iostream>
#include "person.h"

int main() {
    std::cout << "Program starting." << std::endl;
    std::cout << "Creating person..." << std::endl;

    Person p("John", "Doe", 30);

    std::cout << "Person created." << std::endl;
    std::cout << "Name: " << p.getFullname() << std::endl;
    std::cout << "Age: " << p.getAge() << std::endl;

    std::cout << "Person has now birthday..." << std::endl;
    p.ageUp();
    std::cout << "New age: " << p.getAge() << std::endl;

    std::cout << "Program ending." << std::endl;
    return 0;
}
