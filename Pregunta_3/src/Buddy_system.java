import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
public class Buddy_system {
	// Inner class to store lower 
    // and upper bounds of the allocated memory 
    class Pair { 
          
        int lb, ub;
        String nm;
   
        Pair(int a, int b, String name) 
        { 
            lb = a; 
            ub = b;
            nm=name;
        }
        void printPair() {
        	System.out.println(lb +"--------"+   ub);
        }
        
        int getFirt() {
        	return lb;
        }
        int getSecod() {
        	return ub;
        }
        void setname(String name) {
        	this.nm=name;
        }
    } 
  
    // Size of main memory 
    int size; 
  
    // Array to track all 
    // the free nodes of various sizes 
    ArrayList<Pair> arr[]; 
      
    // Hashmap to store the starting 
    // address and size of allocated segment 
    // Key is starting address, size is value 
    HashMap<Integer, Integer> hm; 
    HashMap<String, Integer> mapper; 
      
    // Else compiler will give warning 
    // about generic array creation 
    @SuppressWarnings("unchecked") 
    Buddy_system(int s) { 
          
        size = s; 
        hm = new HashMap<>();
        mapper=new HashMap<>();
          
        // Gives us all possible powers of 2 
        int x = (int)Math.ceil(Math.log(s) / Math.log(2)); 
  
        // One extra element is added 
        // to simplify arithmetic calculations 
        arr = new ArrayList[x + 1]; 
  
        for (int i = 0; i <= x; i++) 
            arr[i] = new ArrayList<>(); 
  
        // Initially, only the largest block is free 
        // and hence is on the free list 
        arr[x].add(new Pair(0, size - 1,"none")); 
    } 
      
    void allocate(int s, String name) 
    { 
    	for (String i : mapper.keySet()) {
    			if(i==name) {
    				 System.out.println("El nombre ya se encuentra reservando memoria, asegurece de que el nombre es correcto y en caso de que lo sea desasigne y asigne el espacio total");
    				 return;
    			}
    	      
    	    }
        // Calculate which free list to search to get the 
        // smallest block large enough to fit the request 
        int x = (int)Math.ceil(Math.log(s) / Math.log(2)); 
  
        int i; 
        Pair temp = null; 
  
        // We already have such a block 
        if (arr[x].size() > 0) { 
  
            // Remove from free list 
            // as it will be allocated now 
            temp = (Pair)arr[x].remove(0);
            temp.setname(name);
            System.out.println("Memoria del bloque " + temp.lb 
                            + " al bloque " + temp.ub + " recervada "+"Por "+temp.nm); 
                              
            // Store in HashMap
            mapper.put(name, temp.lb);
            hm.put(temp.lb, temp.ub - temp.lb + 1); 
            return; 
        } 
  
        // If not, search for a larger block 
        for (i = x + 1; i < arr.length; i++) { 
  
            if (arr[i].size() == 0) 
                continue; 
  
            // Found a larger block, so break 
            break; 
        } 
  
        // This would be true if no such block was found 
        // and array was exhausted 
        if (i == arr.length) { 
              
            System.out.println("Error al recervar memoria"); 
            return; 
        } 
  
        // Remove the first block 
        temp = (Pair)arr[i].remove(0); 
  
        i--; 
  
        // Traverse down the list 
        for (; i >= x; i--) { 
  
            // Divide the block in two halves 
            // lower index to half-1 
            Pair newPair = new Pair(temp.lb, temp.lb 
                                    + (temp.ub - temp.lb) / 2,"none"); 
  
            // half to upper index 
            Pair newPair2 = new Pair(temp.lb 
                                    + (temp.ub - temp.lb + 1) / 2, 
                                    temp.ub,"none"); 
  
            // Add them to next list 
            // which is tracking blocks of smaller size 
            arr[i].add(newPair); 
            arr[i].add(newPair2); 
  
            // Remove a block to continue the downward pass 
            temp = (Pair)arr[i].remove(0); 
        } 
  
        // Finally inform the user 
        // of the allocated location in memory 
        temp.setname(name);
        System.out.println("Memoria del bloque " + temp.lb 
                        + " al bloque  " + temp.ub + " recervada por "+temp.nm); 
  
        // Store in HashMap 
        mapper.put(name, temp.lb);
        hm.put(temp.lb, temp.ub - temp.lb + 1); 
      
    } 
    void deallocate(String name) 
    { 
    	int s=mapper.get(name);
        // Invalid reference, as this was never allocated 
        if (!hm.containsKey(s)) { 
            System.out.println("Solicitud de lieberacion invalida"); 
            return; 
        } 
  
        // Get the list which will track free blocks  
        // of this size 
        int x = (int)Math.ceil(Math.log(hm.get(s))  
                                        / Math.log(2)); 
        int i, buddyNumber, buddyAddress; 
  
        // Add it to the free list 
        arr[x].add(new Pair(s, s + (int)Math.pow(2, x) - 1,"none")); 
        System.out.println("Memoria recervada por " + name +" del bloque "+ s + " al " 
                           + (s + (int)Math.pow(2, x) - 1) + " liberada"); 
  
  
        // Calculte it's buddy number and buddyAddress. The 
        // base address is implicitly 0 in this program, so no 
        // subtraction is necessary for calculating buddyNumber 
        buddyNumber = s / hm.get(s); 
      
        if (buddyNumber % 2 != 0) { 
            buddyAddress = s - (int)Math.pow(2, x); 
        } 
          
        else { 
            buddyAddress = s + (int)Math.pow(2, x); 
        } 
          
          
        // Search in the free list for buddy 
        for (i = 0; i < arr[x].size(); i++) { 
              
              
            // This indicates the buddy is also free 
            if (arr[x].get(i).lb == buddyAddress) { 
                  
                // Buddy is the block after block  
                // with this base address 
                if (buddyNumber % 2 == 0) { 
                      
                    // Add to appropriate free list 
                    arr[x + 1].add(new Pair(s, s  
                                  + 2 * ((int)Math.pow(2, x)) - 1,"none")); 
                    System.out.println("Union de bloques a partir de "
                                            + s + " y "
                                            + buddyAddress + " realizado correctamente"); 
                } 
                  
                // Buddy is the block before block  
                // with this base address 
                else { 
                      
                    // Add to appropriate free list 
                    arr[x + 1].add(new Pair(buddyAddress, 
                                    buddyAddress + 2 * ((int)Math.pow(2, x))- 1,"none")); 
                    System.out.println("Union de bloques a partir de "
                                                + buddyAddress + " y " 
                                                + s + " realizado correctamente "); 
                } 
  
                // Remove the individual segements  
                // as they have coalesced 
                arr[x].remove(i); 
                arr[x].remove(arr[x].size() - 1); 
                break; 
            } 
        } 
  
        // Remove entry from HashMap 
        hm.remove(s);
        mapper.remove(name);
    } 
    void PrintFreeAllocate() {

    	ArrayList<Integer> espacios = new ArrayList<Integer>();
    	for(int i=0;i<arr.length;i++) {
    		if(arr[i].size()>0) {
    			espacios.add(i);
    		}
 
    	}
  
    	if(espacios.size()>0) {
    			if(espacios.size()==1) {
    				 Pair temp = (Pair)arr[espacios.get(0)].get(0);
        			 System.out.println("Hay espacio libre  del bloque "+temp.getFirt()+" al bloque "+temp.getSecod());

        			
    			}else {
    				for(int i=0;i<espacios.size();i++) {
    					 Pair temp = (Pair)arr[espacios.get(i)].get(0);
            			 System.out.println("Hay espacio libre  del bloque "+temp.getFirt()+" al bloque "+temp.getSecod());
    		 
    		    	}
 
    			}
    			
    		}else {
    			System.out.println("No hay ningun bloque libre");
    		}
    	for (String i : mapper.keySet()) {
		      System.out.println("Memoria reservada por "+ i +" "+hm.get(mapper.get(i))+ " bytes");
		 }
		
    	
    		
    	
    }
    public static boolean isAlpha(String s)
    {
        if (s == null) {
            return false;
        }
 
        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);
            if (!(c >= 'A' && c <= 'Z') && !(c >= 'a' && c <= 'z')) {
                return false;
            }
        }
        return true;
    }
     
    private static Scanner input =new Scanner(System.in);
    private static Scanner acciones =new Scanner(System.in);
    public static void main(String args[]) throws IOException 
    { 

          
   
        

        
    	
        HashMap<String,Integer> map=new HashMap<>();
        map.put("SALIR", 1);
        map.put("MOSTRAR", 2);
        map.put("RESERVAR", 0);
        map.put("LIBERAR", 3);
        System.out.println("ingrese la cantidad de bloques de memoria con las que va a trabajar el Programa");
    	int  initialMemory =input.nextInt();
        Buddy_system obj = new Buddy_system(initialMemory); 
        System.out.println("Ingrese una accion");
        while (true){
        	String accion=acciones.nextLine();
        	String[] acc = accion.split(" ");
      
        	if(acc.length==1) {
        		if(map.containsKey(acc[0])&& map.get(acc[0])==1) {
        			  System.out.println("Saliendo del programa...");
        			  break;
        		}else if(map.containsKey(acc[0])&& map.get(acc[0])==2){
        			obj.PrintFreeAllocate();
        		
        		}else {
        			 System.out.println("accion incorrecta");
        		}

        	}else if(acc.length==3) {
        		boolean isnumeric=acc[2].matches("[+-]?\\d*(\\.\\d+)?");
        		boolean iscaracter=isAlpha(acc[1]);

        		if(!map.containsKey(acc[0])|| isnumeric==false || iscaracter==false) {
        			 System.out.println("accion incorrecta");
        		}
        		else if(map.get(acc[0])==0) {
        		  int numEntero = Integer.parseInt(acc[2]) ;
      			  obj.allocate(numEntero, acc[1]);
        		}else {
        			 System.out.println("accion incorrecta");
        		}
        	}
        	else if(acc.length==2) {
        		boolean iscaracterr=isAlpha(acc[1]);
        		if(!map.containsKey(acc[0]) || iscaracterr==false) {
       			 	System.out.println("accion incorrecta");
        		}else if(map.get(acc[0])==3){
        			obj.deallocate(acc[1]);
        		}else {
        			System.out.println("accion incorrecta");
        		}
        	}else {
        		System.out.println("accion incorrecta");
        	}
        	
        }
    } 

}
