package ejercicio2;

import java.util.ArrayList;
import java.util.List;


public class Departamento {
    private String nombre;
    private String area;
    private List<Empleado> empleados;

    public Departamento(String nombre,String area){
        this.nombre = nombre;
        this.area  = area;
        this.empleados = new ArrayList<>();
    }

    public void agregarEmpleado(Empleado empleado){
        this.empleados.add(empleado);
    }

    public boolean removerEmpleado(Empleado empleado){
        return this.empleados.remove(empleado);
    }
    public void mostrarEmpleados(){
        System.out.println("  Departamento:" +nombre+"(" +area+") ");
        if (empleados.isEmpty()){
            System.out.println("[Sin empleados]");
        } else{
            for(Empleado emp:empleados){
                System.out.println(emp);
            }
        }
    }
    public void cambioSalario(double porcentaje){
        System.out.println(" Aplicando cambio de salario (" +porcentaje+"%) en "+ nombre+" ---");
        for (Empleado emp: empleados){
            double salarioActual = emp.getSueldo();
            double nuevoSalario = salarioActual * (1 +(porcentaje/100.0));
            emp.setSueldo(nuevoSalario);
            System.out.println(" "+ emp.getNombre()+ ": Sueldo anterior $" +String.format("%.2f", salarioActual) + ", Nuevo Sueldo $" + String.format("%.2f", nuevoSalario));
        }
    }
    public List<Empleado> getEmpleados(){
        return empleados;
    }
    public String getNombre(){
        return nombre;
    }
}
