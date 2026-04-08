public class Person {
    public String first_name;
    public String last_name;
    private int age;

    public Person(String fname, String lname, int age) {
        this.first_name = fname;
        this.last_name = lname;
        this.age = age;
    }

    public int getAge() {
        return age;
    }

    public void ageUp() {
        age += 1;
    }

    public String getFullname() {
        return first_name + " " + last_name;
    }

    public void printFullname() {
        System.out.println(getFullname());
    }
}
