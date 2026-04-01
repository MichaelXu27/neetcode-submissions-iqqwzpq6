static class Singleton {

    private static volatile Singleton singleInstance = null;
    private String valueString = null;

    private Singleton() {
        
    }

    public static Singleton getInstance() {
        if (singleInstance == null){
            synchronized(Singleton.class){
                if (singleInstance == null){
                    singleInstance = new Singleton();
                } 
            }
        }
        return singleInstance;
    }

    public String getValue() {
        return this.valueString;
    }

    public void setValue(String value) {
        this.valueString = value;
    }
    
}
