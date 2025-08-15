export type Phone = {
  id: number;
  brand: string;
  model: string;
  condition: string;
  specs: Record<string, string>;
  stock: number;
  base_price: number;
  tags: string[];
  manual_price_overrides: Partial<Record<"X" | "Y" | "Z", number>>;
};

export type PhoneCreate = Omit<Phone, "id">;
export type PhoneUpdate = Omit<Phone, "id">;

export type ListingResult = {
  success: boolean;
  platform?: string;
  price?: number;
  mapped_condition?: string;
  error?: string;
};

export type ManualOverride = {
  X?: number;
  Y?: number;
  Z?: number;
};
