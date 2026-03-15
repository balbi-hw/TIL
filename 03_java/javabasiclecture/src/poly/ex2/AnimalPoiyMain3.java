package poly.ex2;

public class AnimalPoiyMain3 {

    public static void main(String[] args) {

        Animal a = new Animal();
        a.sound();

        Animal[] animalArr = {new Dog(), new Cat(), new Caw()};

        for (Animal animal : animalArr) {
            soundAnimal(animal);
        }
    }

    private static void soundAnimal(Animal animal) {
        System.out.println("동물 테스트 시작");
        animal.sound();
        System.out.println("동물 테스트 종료");
    }
}
