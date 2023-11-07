import java.rmi.*;

public class Server extends UnicastRemoteObject implements Adder1{  

    public Server() throws RemoteException{  
        super();  
    }  

    public int add(int x,int y){  
        return x + y;
    }  
}
