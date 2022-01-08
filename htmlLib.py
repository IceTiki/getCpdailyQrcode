# 复制源自https://tool.g3w.cn/jrxy/

flowCss="""<style type="text/css">
            .bg-lv1[data-v-09009c6b] {
                background-color: #f4f4f4
            }

            .bg-lv2[data-v-09009c6b] {
                background-color: #f9f9f9
            }

            .bg-lv3[data-v-09009c6b] {
                background-color: #fff
            }

            .thin-line[data-v-09009c6b] {
                position: absolute;
                display: block;
                top: 0;
                left: 0;
                width: 200%;
                height: 200%;
                transform: scale(.5);
                transform-origin: 0 0;
                -webkit-transform: scale(.5);
                -webkit-transform-origin: 0 0;
                box-sizing: border-box;
                pointer-events: none
            }

            .loc__tip--success[data-v-09009c6b]:before {
                background-color: #7fce38
            }

            .loc__tip--failed[data-v-09009c6b]:before,
            .loc__tip--success[data-v-09009c6b]:before {
                content: "";
                width: .5rem;
                height: .5rem;
                line-height: .5rem;
                margin-right: .4rem;
                display: inline-block;
                border-radius: 50%
            }

            .loc__tip--failed[data-v-09009c6b]:before {
                background-color: #ed5c00
            }

            .tip-color[data-v-09009c6b] {
                color: #92969c
            }

            .mt-8[data-v-09009c6b] {
                margin-top: 8px
            }

            .mt-10[data-v-09009c6b] {
                margin-top: 10px
            }

            .mt-16[data-v-09009c6b] {
                margin-top: 16px
            }

            .mt-24[data-v-09009c6b] {
                margin-top: 24px
            }

            .mb-8[data-v-09009c6b] {
                margin-bottom: 8px
            }

            .mb-10[data-v-09009c6b] {
                margin-bottom: 10px
            }

            .mb-16[data-v-09009c6b] {
                margin-bottom: 16px
            }

            .mb-24[data-v-09009c6b] {
                margin-bottom: 24px
            }

            .mv-8[data-v-09009c6b] {
                margin: 8px 0
            }

            .mv-10[data-v-09009c6b] {
                margin: 10px 0
            }

            .mv-16[data-v-09009c6b] {
                margin: 16px 0
            }

            .mv-24[data-v-09009c6b] {
                margin: 24px 0
            }

            .leave-detail[data-v-09009c6b] {
                position: relative;
                background-color: #fff
            }

            .leave-detail .audit-pass[data-v-09009c6b] {
                position: absolute;
                z-index: 1;
                right: 16px;
                top: 48px;
                width: 80px
            }

            .leave-detail .detail__subtitle[data-v-09009c6b] {
                line-height: 1.5rem;
                padding-left: .75rem;
                color: #bdc0c5;
                background-color: #f4f6f8;
                font-size: .7rem
            }

            .leave-detail .detail__item[data-v-09009c6b] {
                margin-top: .1rem;
                display: flex;
                font-size: .7rem
            }

            .leave-detail .detail__item .detail_item__label[data-v-09009c6b] {
                width: 4.5rem;
                color: #92969c
            }

            .leave-detail .detail__item .detail_item__value[data-v-09009c6b] {
                flex: 1 0 0;
                overflow-wrap: break-word;
                word-break: break-all
            }

            .leave-detail .detail__item .detail_item__value .detail_item__value--danger[data-v-09009c6b] {
                color: #ed3f14
            }

            .leave-detail .detail__item .out__school[data-v-09009c6b] {
                display: flex;
                align-items: center
            }

            .detail__main[data-v-09009c6b] {
                padding: .75rem;
                background-color: #fff;
                position: relative
            }

            .detail__main[data-v-09009c6b]:before {
                position: absolute;
                display: block;
                top: 0;
                width: 200%;
                height: 200%;
                transform: scale(.5);
                transform-origin: 0 0;
                -webkit-transform: scale(.5);
                -webkit-transform-origin: 0 0;
                box-sizing: border-box;
                pointer-events: none;
                content: "";
                left: 0;
                border-top: 1px solid #e9eaec;
                border-bottom: 1px solid #e9eaec
            }

            .detail__content[data-v-09009c6b] {
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 2.4rem;
                overflow-y: scroll;
                color: #1c2438
            }

            .bottom-0[data-v-09009c6b] {
                bottom: 0 !important
            }

            .detail__main__header[data-v-09009c6b] {
                margin-bottom: .4rem
            }

            .detail__comment[data-v-09009c6b] {
                padding: .75rem;
                background-color: #fff;
                position: relative
            }

            .detail__comment[data-v-09009c6b]:before {
                position: absolute;
                display: block;
                top: 0;
                width: 200%;
                height: 200%;
                transform: scale(.5);
                transform-origin: 0 0;
                -webkit-transform: scale(.5);
                -webkit-transform-origin: 0 0;
                box-sizing: border-box;
                pointer-events: none;
                content: "";
                left: 0;
                border-top: 1px solid #e9eaec;
                border-bottom: 1px solid #e9eaec
            }

            .detail__audit__date[data-v-09009c6b] {
                float: right;
                font-size: .6rem;
                color: #bdc0c5
            }

            .detail__comment__desc[data-v-09009c6b] {
                font-size: .7rem
            }

            .status-complete .detail__content[data-v-09009c6b],
            .status-processing .detail__content[data-v-09009c6b] {
                bottom: 0
            }

            .status-complete .detail__bottom[data-v-09009c6b],
            .status-processing .detail__bottom[data-v-09009c6b] {
                display: none
            }

            .btn-area[data-v-09009c6b] {
                padding: .6rem 0;
                overflow: hidden
            }

            .btn-processing[data-v-09009c6b] {
                display: block;
                margin: .4rem 1rem;
                transform: translateZ(0)
            }

            .btn-processing--share[data-v-09009c6b] {
                color: #2f343b;
                background-color: #fff;
                border: 1px solid #dddee1
            }
        </style>"""

flowCss_2="""<style type="text/css">
            @keyframes move {
                0% {
                    color: inherit
                }

                to {
                    background-position: 60px 0
                }
            }

            .status-flag {
                font-size: 0;
                height: 110px
            }

            .status-flag .flag-dom {
                width: 100%;
                height: 100%;
                display: flex;
                flex-direction: column;
                align-items: center;
                color: #fff
            }

            .status-flag .flag-dom .status-text-bold {
                font-weight: 400;
                font-style: normal;
                font-size: 32px;
                letter-spacing: 4px;
                color: #fff;
                line-height: 32px;
                margin-top: 5px
            }

            .status-flag .flag-dom .status-svg-text {
                font-family: Microsoft YaHei Regular, Microsoft YaHei;
                font-weight: 400;
                font-style: normal;
                color: #fff;
                display: flex;
                align-items: center;
                font-size: 16px;
                margin-top: -5px;
                letter-spacing: 2px
            }

            .status-flag .flag-dom .status-svg-text .svg-icon {
                margin-right: 5px;
                margin-top: 7px
            }

            .status-flag .flag-dom .flag-text {
                flex: 1;
                display: flex;
                align-items: center;
                flex-direction: column;
                justify-content: center
            }

            .status-flag .flag-dom .no-shrink {
                flex-shrink: 0
            }

            .status-flag .flag-dom .dynamic-strip {
                width: 100%;
                height: 16px;
                margin: 0 auto;
                background-size: 60px 60px;
                display: flex;
                align-items: center;
                justify-content: center;
                background-image: linear-gradient(135deg, #fff, #fff 25%, transparent 0, transparent 50%, #fff 0, #fff 75%, transparent 0, transparent 0);
                animation: move 1s linear infinite;
                -webkit-animation: move 1s linear infinite
            }

            .status-flag .flag-dom .dynamic-strip .now-time {
                background: rgba(0, 0, 0, .5);
                color: #fff;
                text-align: center;
                padding: 0 5px;
                font-size: 12px;
                border-radius: 7px
            }

            .status-flag .flag-warning {
                background: linear-gradient(180deg, #f66c08 1%, #f8aa24)
            }

            .status-flag .flag-success {
                background: linear-gradient(180deg, #00a857, #00dd73)
            }

            .status-flag .flag-error {
                background: linear-gradient(180deg, #f40, #f79677 97%)
            }

            .status-flag .flag-grey {
                background: linear-gradient(0deg, #9ea7b4, #657180)
            }
        </style>"""

css="""<link type="text/css" rel="stylesheet" href="./xx/index.css">"""

div_1="""<div data-v-09009c6b="" class="status-flag">





            <div class="flag-dom flag-success">
        <span class="grxx">个人信息 &gt;</span>
                <div class="flag-text">
                    <div class="status-svg-text">
                        <div class="pick-svg svg-icon">
                            <svg version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="17px" height="17px" xmlns="http://www.w3.org/2000/svg">
                                <g transform="matrix(1 0 0 1 -134 -146 )">
                                    <path d="M 14.01171875 7.205078125  C 14.14453125 7.072265625  14.2109375 6.90625  14.2109375 6.70703125  C 14.2109375 6.50043402777778  14.14453125 6.33072916666666  14.01171875 6.19791666666666  L 13.0045572916667 5.20182291666666  C 12.8643663194444 5.06163194444444  12.6983506944445 4.99153645833334  12.5065104166667 4.99153645833334  C 12.3146701388889 4.99153645833334  12.1486545138889 5.06163194444444  12.0084635416667 5.20182291666666  L 7.49283854166671 9.70638020833333  L 4.99153645833329 7.205078125  C 4.85134548611107 7.06488715277778  4.68532986111107 6.99479166666666  4.49348958333329 6.99479166666666  C 4.30164930555557 6.99479166666666  4.13563368055557 7.06488715277778  3.99544270833329 7.205078125  L 2.98828125 8.201171875  C 2.85546875 8.333984375  2.7890625 8.50368923611111  2.7890625 8.71028645833334  C 2.7890625 8.90950520833333  2.85546875 9.07552083333333  2.98828125 9.20833333333333  L 6.99479166666671 13.21484375  C 7.13498263888893 13.3550347222222  7.30099826388893 13.4251302083333  7.49283854166671 13.4251302083333  C 7.69205729166671 13.4251302083333  7.86176215277778 13.3550347222222  8.001953125 13.21484375  L 14.01171875 7.205078125  Z M 15.8600260416667 4.2333984375  C 16.6200086805556 5.53569878472222  17 6.95789930555555  17 8.5  C 17 10.0421006944444  16.6200086805556 11.4643012152778  15.8600260416667 12.7666015625  C 15.1000434027778 14.0689019097222  14.0689019097222 15.1000434027778  12.7666015625 15.8600260416667  C 11.4643012152778 16.6200086805556  10.0421006944444 17  8.5 17  C 6.95789930555557 17  5.53569878472222 16.6200086805556  4.2333984375 15.8600260416667  C 2.93109809027779 15.1000434027778  1.89995659722221 14.0689019097222  1.13997395833329 12.7666015625  C 0.37999131944443 11.4643012152778  0 10.0421006944444  0 8.5  C 0 6.95789930555555  0.37999131944443 5.53569878472222  1.13997395833329 4.2333984375  C 1.89995659722221 2.93109809027778  2.93109809027779 1.89995659722222  4.2333984375 1.13997395833333  C 5.53569878472222 0.379991319444438  6.95789930555557 0  8.5 0  C 10.0421006944444 0  11.4643012152778 0.379991319444438  12.7666015625 1.13997395833333  C 14.0689019097222 1.89995659722222  15.1000434027778 2.93109809027778  15.8600260416667 4.2333984375  Z " fill-rule="nonzero" fill="#ffffff" stroke="none" transform="matrix(1 0 0 1 134 146 )"></path>
                                </g>
                            </svg></div> <span>审批已通过</span>
                    </div>
                    <div class="status-text-bold">
                        正在休假中
                    </div>
                </div>
                <div class="dynamic-strip no-shrink">
                    <div class="now-time">
                        <span id="nowTime">当前时间： 2022-01-08 08:09:03　</span>
                    </div>
                </div>
            </div>
        </div>"""

timeJs="""<script type="text/javascript">
    var newDate = '';
    getLangDate();

    function dateFilter(date) { //值小于10时，在前面补0
        if (date < 10) {
            return "0" + date;
        }
        return date;
    }

    function getLangDate() {
        var dateObj = new Date(); //表示当前系统时间的Date对象
        var year = dateObj.getFullYear(); //当前系统时间的完整年份值
        var month = dateObj.getMonth() + 1; //当前系统时间的月份值
        var date = dateObj.getDate(); //当前系统时间的月份中的日
        var day = dateObj.getDay(); //当前系统时间中的星期值
        var weeks = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"];
        var week = weeks[day]; //根据星期值，从数组中获取对应的星期字符串
        var hour = dateObj.getHours(); //当前系统时间的小时值
        var minute = dateObj.getMinutes(); //当前系统时间的分钟值
        var second = dateObj.getSeconds(); //当前系统时间的秒钟值
        var timeValue = "" + ((hour >= 12) ? (hour >= 18) ? "晚上" : "下午" : "上午"); //当前时间属于上午、晚上还是下午
        newDate = dateFilter(year) + "-" + dateFilter(month) + "-" + dateFilter(date) + " " + dateFilter(hour) + ":" +
            dateFilter(minute) + ":" + dateFilter(second);
        document.getElementById("nowTime").innerHTML = "当前时间： " + newDate + "　";
        setTimeout(getLangDate, 1000);
    }
</script>"""