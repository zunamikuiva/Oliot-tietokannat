<?php

class Person {
    public $first_name;
    public $last_name;
    private $age;

    public function __construct($fname, $lname, $age) {
        $this->first_name = $fname;
        $this->last_name = $lname;
        $this->age = $age;
    }

    public function getAge() {
        return $this->age;
    }

    public function ageUp() {
        $this->age += 1;
    }

    public function getFullname() {
        return $this->first_name . " " . $this->last_name;
    }

    public function printFullname() {
        echo $this->getFullname() . "\n";
    }
}

echo "Program starting.\n";
echo "Creating person...\n";

$person = new Person("John", "Doe", 30);

echo "Person created.\n";
echo "Name: " . $person->getFullname() . "\n";
echo "Age: " . $person->getAge() . "\n";

echo "Person has now birthday...\n";
$person->ageUp();
$age = $person->getAge();

echo "New age: " . $age . "\n";
echo "Program ending.\n";
