class laptop {
   private int id;
   private int hdd_volume;
   private int ram_volume;
   private int display_size;
   private String os_type;
   private String color;
   private String brand;

   public laptop (int id, int hdd_volume, int ram_volume, int display_size, String os_type, String color,
                         String brand) {
      this.id = id;
      this.hdd_volume = hdd_volume;
      this.ram_volume = ram_volume;
      this.display_size = display_size;
      this.os_type = os_type;
      this.color = color;
      this.brand = brand;
   }


   @Override
   public int hashCode() {
      final int prime = 31;
      int result = 1;
      result = prime * result + ((brand == null) ? 0 : brand.hashCode());
      result = prime * result + ((color == null) ? 0 : color.hashCode());
      result = prime * result + display_size;
      result = prime * result + hdd_volume;
      result = prime * result + id;
      result = prime * result + ((os_type == null) ? 0 : os_type.hashCode());
      result = prime * result + ram_volume;
      return result;
   }

   @Override
   public boolean equals(Object obj) {
      if (this == obj)
         return true;
      if (obj == null)
         return false;
      if (getClass() != obj.getClass())
         return false;
      laptop   other = (laptop) obj;
      if (brand == null) {
         if (other.brand != null)
            return false;
      } else if (!brand.equals(other.brand))
         return false;
      if (color == null) {
         if (other.color != null)
            return false;
      } else if (!color.equals(other.color))
         return false;
      if (display_size != other.display_size)
         return false;
      if (hdd_volume != other.hdd_volume)
         return false;
      if (id != other.id)
         return false;
      if (os_type == null) {
         if (other.os_type != null)
            return false;
      } else if (!os_type.equals(other.os_type))
         return false;
      if (ram_volume != other.ram_volume)
         return false;
      return true;
   }

   public int getId() {
      return id;
   }

   public void setId(int id) {
      this.id = id;
   }

   public int getHDDvolume() {
      return hdd_volume;
   }

   public void setHDDvolume(int volume) {
      this.hdd_volume = volume;
   }

   public int getRAMvolume() {
      return ram_volume;
   }

   public void setRAMvolume(int volume) {
      this.ram_volume = volume;
   }

   public int getDisplSize() {
      return display_size;
   }

   public void setDisplSize(int size) {
      this.display_size = size;
   }

   public String getBrand() {
      return brand;
   }

   public void setBrand(String name) {
      this.brand = name;
   }

   public String getColor() {
      return color;
   }

   public void setColor(String color) {
      this.color = color;
   }

   public String getOStype() {
      return os_type;
   }

   public void setOStype(String type) {
      this.os_type = type;
   }

   @Override
   public String toString() {
      return "{id=" + id + ",  brand=" + brand + ", color=" + color + ", display_size=" + display_size + ", hdd_volume="
              + hdd_volume + ",  ram_volume=" + ram_volume+",  os_type=" + os_type+ "}";
   }

}