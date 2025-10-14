/**
 * 枚举：订单状态
 */
export enum OrderStatus {
  /** 待支付 */
  PENDING_PAYMENT = 'pending_payment',
  /** 已支付 */
  PAID = 'paid',
  /** 已发货 */
  SHIPPED = 'shipped',
  /** 已完成 */
  COMPLETED = 'completed',
  /** 已取消 */
  CANCELLED = 'cancelled',
}