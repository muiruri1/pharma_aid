$(function() {
    $(document).on("click", ".list-item-button", function(e) {
        e.preventDefault();

        var slug = $(this).attr('data-slug');
        var url = '/cart/add/' + slug + '/';

        $.ajax({
            type: "GET",
            url: url,

            success: function(data) {
                $("#" + slug + "_quantity_in_bag").text(data.quantity);
                $("#" + slug + "_total").text(data.total);

                $("#bag-item-number").html(data.total_item);
                $("#bag-taka-number").html(data.total_taka);
                $("#big-bag-item-number").html(data.total_item);
                $("#big-bag-taka-number").html(data.total_taka);

                if ($("#cart-item-" + data.cart_item_id).length == 0) {
                    $("#big-bag-body").append('<div class="bag-item" id="cart-item-' + data.cart_item_id + '"> \
                                                    <div class="left-control"> \
                                                        <div class="qty_up" data-slug="' + slug + '"><center><i class="fa fa-sort-up left-control-button"></i></center></div> \
                                                        <div class="quantity"><center id="' + slug + '_quantity_in_bag">' + data.quantity + '</center></div> \
                                                        <div class="qty_down" data-slug="' + slug + '"><center><i class="fa fa-sort-down left-control-button"></i></center></div> \
                                                    </div> \
                                                    <div class="product_img"><img src="https://placeholdit.imgix.net/~text?&w=30&h=30"/></div> \
                                                    <div class="product_details"> \
                                                        <div class="product_name">' + data.cart_item_name + '</div> \
                                                        <div class="product_price"> \
                                                            <small>Tk. ' + data.cart_item_price + ' / box</small> \
                                                        </div> \
                                                    </div> \
                                                    <div class="total" id="' + slug + '_total">' + data.total + '</div> \
                                                    <div class="remove cart-item-remove" data-slug="' + slug + '"> \
                                                        <i class="fa fa-close"></i> \
                                                    </div> \
                                                </div>');
                    }
            }
        });
    });

    $(document).on("click", ".qty_up", function(e) {
        e.preventDefault();

        var slug = $(this).attr('data-slug');
        var url = '/cart/add/' + slug + '/';

        $.ajax({
            type: "GET",
            url: url,

            success: function(data) {
                $("#" + slug + "_quantity_in_bag").text(data.quantity);
                $("#" + slug + "_total").text(data.total);

                $("#bag-item-number").html(data.total_item);
                $("#bag-taka-number").html(data.total_taka);
                $("#big-bag-item-number").html(data.total_item);
                $("#big-bag-taka-number").html(data.total_taka);
            }
        })
    });

    $(document).on("click", ".qty_down", function(e) {
        e.preventDefault();

        var slug = $(this).attr('data-slug');
        var url = '/cart/remove/' + slug + '/';

        $.ajax({
            type: "GET",
            url: url,

            success: function(data) {
                $("#" + slug + "_quantity_in_bag").text(data.quantity);
                $("#" + slug + "_total").text(data.total);

                $("#bag-item-number").html(data.total_item);
                $("#bag-taka-number").html(data.total_taka);
                $("#big-bag-item-number").html(data.total_item);
                $("#big-bag-taka-number").html(data.total_taka);
            }
        })
    });

    $(document).on("click", ".cart-item-remove", function(e) {
        e.preventDefault();

        var slug = $(this).attr('data-slug');
        var url = '/cart/delete/' + slug + '/';

        $.ajax({
            type: "GET",
            url: url,

            success: function(data) {
                $("#cart-item-" + data.item_id).remove();

                $("#bag-item-number").html(data.total_item);
                $("#bag-taka-number").html(data.total_taka);
                $("#big-bag-item-number").html(data.total_item);
                $("#big-bag-taka-number").html(data.total_taka);
            }
        })
    });
});
