class ClassTest:
    def instance_method(self):
         print(f"Called instance_method of {self}")

    @classmethod  #this way, we dont need a instance.
    def class_method(cls):
         print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
         print("Called static_method.")


test = ClassTest() #creation new objet
test.instance_method()
#ClassTest.instance_method(test) the same code with upper code.





# Python'daki sınıf metodları ve statik metodlar, sınıf içindeki metotlardır. Ancak bu iki tür metodun farklı kullanım amaçları ve özellikleri vardır.

# Sınıf metodları, sınıfın kendisine ait özelliklere ve metodlara erişebilen bir metod türüdür. Bu metotlara erişmek için sınıfın adı kullanılır. Sınıf metodları, sınıfın tüm örnekleri tarafından paylaşılan özellikleri veya davranışları yönetmek için kullanılabilir. Sınıf metodları, @classmethod dekoratörü kullanılarak tanımlanır.

# Statik metodlar, sınıfın özelliklerine veya örneklerine erişemeyen bir metod türüdür. Bu metotlar, sınıfın içinde yer alır, ancak sınıfın özelliklerine veya örneklerine erişmek için herhangi bir parametre almazlar. Statik metodlar, sınıfın fonksiyonelitesine veya örnekleriyle ilişkili olmayan bir yardımcı işlevi yerine getirmek için kullanılabilir. Statik metodlar, @staticmethod dekoratörü kullanılarak tanımlanır.

# Sınıf metodları ve statik metodlar arasındaki ana fark, erişebildikleri özelliklerdir. Sınıf metodları sınıfın özelliklerine erişebilirken, statik metodlar sadece kendi içlerindeki özelliklere erişebilir. Ayrıca sınıf metodları sınıfın örnekleri tarafından da çağrılabilirken, statik metodlar sadece sınıf adıyla çağrılabilir.

# Sınıf metodları ve statik metodlar, programın okunabilirliğini ve bakımını kolaylaştırmak için kullanılır. Sınıf metodları, sınıfın tüm örneklerinin paylaştığı özellikleri veya davranışları yönetmek için kullanılırken, statik metodlar sınıfın fonksiyonelliğiyle ilişkisi olmayan yardımcı işlevleri yerine getirmek için kullanılır. Bu metodlar, kodun daha düzenli ve anlaşılır olmasını sağlar ve gerektiğinde kodun yeniden kullanılmasına da olanak tanır.