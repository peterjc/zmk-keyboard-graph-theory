#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/drivers/led.h>
#include <zephyr/init.h>
#include <zephyr/kernel.h>
#include <zmk/events/hid_indicators_changed.h>
#include <zmk/hid_indicators.h>

#define LED_GPIO_NODE_ID DT_COMPAT_GET_ANY_STATUS_OKAY(gpio_leds)

// GPIO-based LED device
static const struct device *led_dev = DEVICE_DT_GET(LED_GPIO_NODE_ID);

static int led_keylock_listener_cb(const zmk_event_t *eh) {
  zmk_hid_indicators_t flags = zmk_hid_indicators_get_current_profile();
  unsigned int capsBit = 1 << (HID_USAGE_LED_CAPS_LOCK - 1);

  if (flags & capsBit) {
    led_on(led_dev, DT_NODE_CHILD_IDX(DT_ALIAS(user_led)));
  } else {
    led_off(led_dev, DT_NODE_CHILD_IDX(DT_ALIAS(user_led)));
  }

  return 0;
}

ZMK_LISTENER(led_indicators_listener, led_keylock_listener_cb);
ZMK_SUBSCRIPTION(led_indicators_listener, zmk_hid_indicators_changed);

static int leds_init(void) {
  if (!device_is_ready(led_dev)) {
    return -ENODEV;
  }

  return 0;
}

// run leds_init on boot
SYS_INIT(leds_init, APPLICATION, CONFIG_APPLICATION_INIT_PRIORITY);
