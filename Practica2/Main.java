import java.util.ArrayList;
import java.util.List;

public class Main {
    public stactic void Main(String[]args){

        Departamento dpto1 = new Departamento("Ventas y Marketing", "Comercial");
        
        Empleado e1 = new Empleado("Ana García", "Gerente de Ventas", 50000.00);
        Empleado e2 = new Empleado("Luis Pérez", "Especialista Marketing", 35000.00);
        Empleado e3 = new Empleado("Marta Soto", "Ejecutiva de Cuentas", 30000.00);
        Empleado e4 = new Empleado("Carlos Ruiz", "Asistente de Ventas", 25000.00);
        Empleado e5 = new Empleado("Elena Díaz", "Analista SEO", 38000.00);

        dpto1.agregarEmpleado(e1);
        dpto1.agregarEmpleado(e2);
        dpto1.agregarEmpleado(e3);
        dpto1.agregarEmpleado(e4);
        dpto1.agregarEmpleado(e5);

        Departamento dpto2 = new Departamento("Investigación y Desarrollo", "Tecnología");
        
        System.out.println("Punto a) Instanciación de departamentos y empleados completada.");

        System.out.println("\n==========================================================");
        System.out.println("Punto b) Mostrar empleados (Verificación inicial)");
        System.out.println("==========================================================");
        dpto1.mostrarEmpleados();
        dpto2.mostrarEmpleados();

        System.out.println("\n==========================================================");
        System.out.println("Punto c) Aplicar cambio de salario (+10% en Dpto 1)");
        System.out.println("==========================================================");
        dpto1.cambioSalario(10.0); // Aumento del 10%

        dpto1.mostrarEmpleados();

        System.out.println("\n==========================================================");
        System.out.println("Punto d) Verificar si empleados de Dpto 1 pertenecen a Dpto 2");
        System.out.println("==========================================================");
        
        boolean encontrado = false;

        for (Empleado emp1 : dpto1.getEmpleados()) {
            if (dpto2.getEmpleados().contains(emp1)) {
                System.out.println("  ¡ATENCIÓN! El empleado " + emp1.getNombre() + " pertenece a ambos departamentos.");
                encontrado = true;
            }
        } 
        if (!encontrado) {
            System.out.println("  Ningún empleado del Departamento 1 pertenece al Departamento 2.");
        }

        System.out.println("\n==========================================================");
        System.out.println("Punto e) Mover empleados de Dpto 1 a Dpto 2");
        System.out.println("==========================================================");


        List<Empleado> empleadosAMover = new ArrayList<>(dpto1.getEmpleados());
        int contadorMovidos = 0;
        
        for (Empleado emp : empleadosAMover) {
            // 1. Remover del Departamento 1 (origen)
            if (dpto1.removerEmpleado(emp)) { 
                // 2. Agregar al Departamento 2 (destino)
                dpto2.agregarEmpleado(emp); 
                contadorMovidos++;
            }
        }

        System.out.println("  Se han movido " + contadorMovidos + " empleados.");

        System.out.println("\n--- Estado Final de los Departamentos ---");
        dpto1.mostrarEmpleados();
        dpto2.mostrarEmpleados();

    }
}