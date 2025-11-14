package ejercicio2;

public class Empleado {
    private String nombre;
    private String cargo;
    private double sueldo;

    public Empleado(String nombre, String cargo, double sueldo){
        this.nombre = nombre;
        this.cargo = cargo;
        this.sueldo = sueldo;
    }
    public String getNombre(){
        return nombre;
    }
    public double getSueldo(){
        return sueldo;
    }
    public void setSueldo(double sueldo){
        this.sueldo = sueldo;
    }
    @Override
    public String toString(){
        return " -> NOmbre; " + nombre + ", Cargo: " + cargo + ", sueldo: $" + String.format("%.2f", sueldo);
    }
    @Override
    public boolean equals(Object obj){
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Empleado empleado = (Empleado) obj;
        return nombre.equals(empleado.nombre) && cargo.equals(empleado.cargo);
    }
    
}
