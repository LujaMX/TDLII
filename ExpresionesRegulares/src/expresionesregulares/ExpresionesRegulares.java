/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package expresionesregulares;

import javax.swing.JOptionPane;

/**
 *
 * @author Luis Portillo
 */
public class ExpresionesRegulares {

    public static MainFrame m = new MainFrame();
    
    public static boolean validarFecha(String fecha){
        
        return fecha.matches("^(?:3[01]|[12][0-9]|0?[1-9])([\\-/.])(0?[1-9]|1[1-2])\\1\\d{4}$");
        
    }
    
    public static boolean validarHora(String hora){
        
        return hora.matches("^([01]?[0-9]|2[0-3]):[0-5][0-9]$");
        
    }
    
    public static boolean validarIP(String ip){
        
        return ip.matches("^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
                + "\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$");
        
    }
    
    public static boolean validarTarjeta(String tarjeta){
        
        return tarjeta.matches("5[1-5][0-9]{14}$");
        
    }
    
    public static boolean validarCurp(String curp){
        
        return curp.matches("^[A-Z]{1}[AEIOU]{1}[A-Z]{2}" +
"[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])" +
"[HM]{1}" +
"(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)" +
"[B-DF-HJ-NP-TV-Z]{3}" +
"[0-9A-Z]{1}" +
"[0-9]{1}$");
        
    }
    
    public static void mostrarMensaje(boolean validador, String expresion){
        if(validador == true){
            JOptionPane.showMessageDialog(null,"La expresion " + expresion + " es aceptada");
        }else{
            JOptionPane.showMessageDialog(null,"La expresion " + expresion + " ha sido rechazada");
        }
    }
    
    public static void main(String[] args) {
        m.setVisible(true);
    }
    
}
